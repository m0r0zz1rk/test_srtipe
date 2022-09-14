import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404

from pay.models import Item, StripeProduct
from pay.serializers import ItemsSerializer, StripeSessionSerializer
from pay.stripe import CreateStripeSessionService


class ItemsListViewSet(viewsets.ReadOnlyModelViewSet):
    """Полуение списка всех товаров"""
    model = Item
    serializer_class = ItemsSerializer

    def get_queryset(self):
        return Item.objects.all()


class ItemDetailViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение детальной информации о товаре"""

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=request.GET.get('pk'))
        serializer = ItemsSerializer(item)
        return JsonResponse(serializer.data)


class CreateStripeSession(viewsets.ViewSet):
    """Создание Stripe Session"""

    def retrieve(self, request, pk=None):
        stripe.api_key = settings.STRIPE_SECRET
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        price_id = StripeProduct.objects.get(item_id=item.id).price_id
        quantity = request.GET.get('quantity')
        session = CreateStripeSessionService(price_id=price_id, quantity=quantity)
        data = {
            'id': session['id'],
            'publish_key': settings.STRIPE_API_KEY
        }
        serializer = StripeSessionSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
