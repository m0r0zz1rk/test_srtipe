from django.urls import path

from .api_views import ItemsListViewSet, CreateStripeSession
from .views import ItemsList

urlpatterns = [
    path('', ItemsList.as_view()),
    path('api/buy/<int:pk>', CreateStripeSession.as_view({'get': 'retrieve'})),
    path('api/item/<int:pk>', ItemsListViewSet.as_view({'get': 'retrieve'})),
    path('api/list_items', ItemsListViewSet.as_view({'get': 'list'})),
]