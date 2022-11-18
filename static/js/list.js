function get_items(){
    $('.content').empty();
    $('.content').append('<img src="static/gif/load.gif">');
    fetch('https://stripe.coko38.ru/api/list_items', {
        method: 'GET',
      })
      .then(res => res.json())
      .then(data => {
        content = '<table><thead><tr><th>Наименование товара</th><th>Описание товара</th><th>Стоимость'
                +'</th><th>Покупка</th></tr></thead><tbody>'
        $.each(data, function (index, rec) {
            content += '<tr><td>'+rec.name+'</td><td>'+rec.description+'</td><td>'+rec.price+'</td>'
                +'<td><button type="button" onclick=\'detail_info('+rec.id+');\'>'
                +'Перейти</button></td></tr>'
        })
        content += '</tbody></table>'
        $('.content').empty();
        $('.content').append(content);
      })
};
function detail_info(id){
    $('.content').empty();
    $('.content').append('<img src="static/gif/load.gif">');
    fetch('https://stripe.coko38.ru/api/item/'+id, {
        method: 'GET',
      })
      .then(res => res.json())
      .then(data => {
        content = '<table><tr>'
                  +'<td>Наименование товара</td><td>'+data.name+'</td></tr>'
                  +'<tr><td>Описание товара</td><td>'+data.description+'</td></tr>'
                  +'<tr><td>Стоимость</td><td>'+data.price+'</td></td>'
                  +'<tr><td>Количество</td><td><input type="number" id="quant" name="quantity" required></td></tr>'
                  +'<tr><td colspan="2"><button type="button" onclick="CreateSession('+data.id+');">Купить</button></td></tr></table>'
                  +'<br><a href="javascript:;" onclick="get_items();">Назад к списку</a>'
        $('.content').empty();
        $('.content').append(content);
    })
};
function CreateSession(item_id){
    var quant = $('#quant').val();
    $('.content').empty();
    $('.content').append('<img src="static/gif/load.gif">');
    fetch('https://stripe.coko38.ru/api/buy/'+item_id+'?quantity='+quant, {
        method: 'GET',
      })
      .then(res => res.json())
      .then(function redirectTo(data){
        console.log(data);
        var stripe = Stripe(data.publish_key);
        return stripe.redirectToCheckout({ sessionId: data.id });
      })
};