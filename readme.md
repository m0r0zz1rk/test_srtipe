### Тестовое задание "API оплаты для сервиса Stripe"
___

#### Назначение

Выполнение тестового задания создания API 
для оплаты товаров сервиса Stripe
___

#### Зависимости
Для корректной работы проекта должны быть установлены:
1. Django Rest Framework;
2. Django-environ;
Для установки зависимостей воспользуйтесь файлом req.txt в корневом каталоге проекта:
`pip install -r req.txt`
___
#### Запуск проекта
Для запуска проекта в корне директории `config` необходимо создать файл `.env`, в который внести следующие параметры:
`SECRET_KEY={KEY}`, где вместо `{KEY}` указать секретный ключ для Django проекта (можно сгенерировать [здесь](https://djecrety.ir/))  
`STRIPE_API_KEY={pk}`, где вместо `{pk}` указать `Publishable key` из сервиса `Stripe`
`STRIPE_SECRET={pk}`, где вместо `{pk}` указать `Secret key` из сервиса `Stripe`

___

#### Приложения
+ `pay` - приложение для работы c оплатой сервиса `Stripe`
___

#### Модели

В приложении `pay` созданы две модели:  
+ `Item` - модель товара, содержащая `name`, `description` и `price`  
  (по тестовому заданию)
+ `StripeProduct` - модель данных для работы сервиса `Stripe`, содержит  
поля `item` (FK с таблицей `Item`), `product_id` (`product_id` соответствующего  
товара из таблицы `Item` для сервиса `Stripe`) и `price_id` (`price_id` для соответствующего  
товара из таблицы `Item` для сервиса `Stripe`)

Сущности в моделе `StripeProduct` создаются автоматически при добавлении нового  
товара в модели `Item` (метод `def save()`). Новые сущности в модели `Item` можно  
добавить из административной панели( логин - `admin`, пароль-`Qaz2wsx3`)

---
#### API

Приложение `pay` содержит следующие эндпоинты:  
`GET /api/buy/<int:pk>?quantity=<int:quantity>` - создание Session сервиса Stripe и последующий  
редирект на страницу оплаты (`pk` принимает id товара из модели `Item`, `quantity` - количество  
покупаемого товара);  
`GET /api/item/<int:pk>` - получение информации о товаре из модели `Item` с id равным `pk`;  
`GET /api/list_items` - получение списка всех товаров из модели `Item`