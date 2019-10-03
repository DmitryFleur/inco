from django.test import TestCase
from inventory_management.interfaces import Inventory


class InventoryInterfaceTestCase(TestCase):

    def setUp(self):
        self.inventory = Inventory()

    def test_get_categories_wrong_type(self):
        with self.assertRaises(TypeError):
            self.inventory.get_categories_for_store('some_dummy_category')

    def test_get_categories_happy_flow(self):
        first_category = self.inventory.get_categories_for_store(1)
        self.assertEqual(first_category, [1, 10, 2])

        sec_category = self.inventory.get_categories_for_store(2)
        self.assertEqual(sec_category, [1, 10])

    def test_get_categories_empty_resp(self):
        categories = self.inventory.get_categories_for_store(99)
        self.assertEqual(categories, [])

    def test_get_median_wrong_type(self):
        with self.assertRaises(TypeError):
            self.inventory.get_categories_for_store('some_dummy_category')

    def test_get_median_happy_flow(self):
        med_price = self.inventory.get_median_for_category(10)
        self.assertEqual(med_price, 56.67)

    def test_get_median_non_exist_category(self):
        med_price = self.inventory.get_median_for_category(99)
        self.assertEqual(med_price, 0)

    def test_get_item_inv_non_esisting_item(self):
        items = self.inventory.get_item_inventory('non_exist')
        self.assertEqual(len(items), 0)

    def test_get_item_inv_happy_flow(self):
        items = self.inventory.get_item_inventory('shorts')
        self.assertEqual(len(items), 1)
        self.assertIn('items', items[0].keys())
        self.assertIn(20, items[0].values())
