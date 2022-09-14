from rest_framework import serializers

from pay.models import Item


class StripeSessionSerializer(serializers.Serializer):
    """Сериалайзер для Stripe Session"""
    id = serializers.CharField()
    publish_key = serializers.CharField()


class StripeProductSerializer(serializers.Serializer):
    """Сериалайзер для Stirpe Product"""
    product_id = serializers.CharField()


class ItemsSerializer(serializers.ModelSerializer):
    """Сериалайзер для сущностей модели товаров"""
    class Meta:
        model = Item
        fields = '__all__'