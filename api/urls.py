from django.urls import path
from api.views import StoreCategoriesView, InventoryView, MedianView

urlpatterns = [
    path('store-categories/<int:store_id>/', StoreCategoriesView.as_view()),
    path('item-inventory/<str:item>/', InventoryView.as_view()),
    path('median/<int:category_id>/', MedianView.as_view())
]
