from django.http import JsonResponse
from django.views import View
from inventory_management.interfaces import Inventory


class StoreCategoriesView(View):

    def get(self, request, store_id):
        inventory = Inventory()
        categories = inventory.get_categories_for_store(store_id)
        return JsonResponse({'res': categories,
                             'error': False})


class InventoryView(View):

    def get(self, request, item):
        inventory = Inventory()
        items = inventory.get_item_inventory(item)
        return JsonResponse({'res': items,
                             'error': False})


class MedianView(View):

    def get(self, request, category_id):
        inventory = Inventory()
        median = inventory.get_median_for_category(category_id)
        return JsonResponse({'res': median,
                             'error': False})
