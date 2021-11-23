from django.test import TestCase

class TestStatusCodePages(TestCase):
    """Test status code different pages """
    # моя ошибка что не использовал reverse!!!

    def test_index_page(self):
        resp = self.client.get('/index/')
        self.assertEqual(resp.status_code, 200)

    def test_shop_detail_page(self):
        resp = self.client.get('/index/1/')
        self.assertEqual(resp.status_code, 200)

    def test_shop_detail2_page(self):
        resp = self.client.get('/index/1/detail/')
        self.assertEqual(resp.status_code, 200)

    def test_shop_update_page(self):
        resp = self.client.get('/index/1/update/')
        self.assertEqual(resp.status_code, 200)

    def test_shop_delete_page(self):
        resp = self.client.get('/index/1/delete/')
        self.assertEqual(resp.status_code, 200)

    def test_department_detail_page(self):
        resp = self.client.get('/index/1/1/')
        self.assertEqual(resp.status_code, 200)

    def test_department_create_page(self):
        resp = self.client.get('/index/1/department/new/')
        self.assertEqual(resp.status_code, 200)

    def test_department_update_page(self):
        resp = self.client.get('/index/1/1/update/')
        self.assertEqual(resp.status_code, 200)

    def test_department_delete_page(self):
        resp = self.client.get('/index/1/1/delete/')
        self.assertEqual(resp.status_code, 200)

    def test_item_detail_page(self):
        resp = self.client.get('/index/1/1/1/')
        self.assertEqual(resp.status_code, 200)

    def test_item_create_page(self):
        resp = self.client.get('/index/1/1/item/new/')
        self.assertEqual(resp.status_code, 200)

    def test_item_update_page(self):
        resp = self.client.get('/index/1/1/1/update/')
        self.assertEqual(resp.status_code, 200)

    def test_item_delete_page(self):
        resp = self.client.get('/index/1/1/1/delete/')
        self.assertEqual(resp.status_code, 200)

    def test_login_page(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    def test_logout_page(self):
        resp = self.client.get('/logout/')
        self.assertEqual(resp.status_code, 200)

    def test_filter_item_page(self):
        resp = self.client.get('/filter/item/1/')
        self.assertEqual(resp.status_code, 200)
        
    def test_filter_shop_page(self):
        resp = self.client.get('/filter/shop/1/')
        self.assertEqual(resp.status_code, 200)

    def test_compare_page(self):
        resp = self.client.get('/nogoods/')
        self.assertEqual(resp.status_code, 200)

    def test_unsold_items(self):
        resp = self.client.get('/unsold_items/')
        self.assertEqual(resp.status_code, 200)

class TestAmountGoods(TestCase):
    """Test amount goods"""
    def setUp(self):
        # create instance, why?
        pass

    def test_amounts_goods_1(self):
        resp = self.client.get('/index/1/')
        self.assertContains(resp, 'Amount goods in shops = 0')
        self.assertContains(resp, 'Sorry, but all goods are sold')

    def test_amounts_goods_2(self):
        resp = self.client.get('/index/1/1/')
        self.assertContains(resp, 'Amount goods in shops = 0')
        self.assertContains(resp, 'Sorry, but all goods are sold')

    def test_amounts_goods_3(self):
        resp = self.client.get('/index/')
        self.assertContains(resp, 'Amount goods in shops = 0')
        self.assertContains(resp, 'Sorry, but all goods are sold')
