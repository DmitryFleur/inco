import json
from pathlib import Path

DEFAULT_INVENTORY = json.load(open(Path(__file__).absolute().parent / './data/inventory.json'))


class Inventory(object):
    """
    Inventory Management system
    """
    def __init__(self, inventory=DEFAULT_INVENTORY):
        self.inventory = inventory

    def get_categories_for_store(self, store):
        """
        Given a store id you should return all the categories ids in the inventory.
        :param store: store id
        :return: all the categories ids in the inventory
        """
        if not isinstance(store, int):
            raise TypeError('Store ID should be int type')

        return list(set([item['category'] for item in self.inventory if item['store'] == store]))

    def get_item_inventory(self, item):
        """
        Given items name return all the items across all stores.
        :param item: item name
        :return: all the items across all stores
        """
        return [item_data for item_data in self.inventory if item_data['item_name'] == item]

    def get_median_for_category(self, category):
        """
        Given category id return the median of the prices for all items in the category.
        :param category: category name
        :return: the median of the prices for all items in the category
        """
        if not isinstance(category, int):
            raise TypeError('Category ID should be int type')

        category_prices = [item['price'] for item in self.inventory if item['category'] == category]
        if category_prices:
            return round(sum(category_prices) / len(category_prices), 2)
        return 0
