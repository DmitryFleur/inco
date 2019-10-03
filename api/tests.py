import json
from django.test import TestCase, Client
from inventory_management.interfaces import Inventory


class InventoryAPITestCase(TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.client = Client()

    def assert_response(self, resp, true_data):
        res_data = json.loads(resp.content)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(res_data['res'], true_data)

    def test_get_categories_for_store_happy_flow(self):
        res = self.client.get('/api/store-categories/1/')
        self.assert_response(res, self.inventory.get_categories_for_store(1))

    def test_get_categories_for_store_non_exist(self):
        res = self.client.get('/api/store-categories/9999/')
        self.assert_response(res, [])

    def test_item_inventory_non_exist(self):
        res = self.client.get('/api/item-inventory/non-exist/')
        self.assert_response(res, [])

    def test_item_inventory_happy_flow(self):
        res = self.client.get('/api/item-inventory/pc/')
        self.assert_response(res, self.inventory.get_item_inventory('pc'))

    def test_median_happy_flow(self):
        res = self.client.get('/api/median/10/')
        self.assert_response(res, self.inventory.get_median_for_category(10))

    def test_median_non_exist(self):
        res = self.client.get('/api/median/9999/')
        self.assert_response(res, 0)
