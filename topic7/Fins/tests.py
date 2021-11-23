from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver


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


class TestSelenium(StaticLiveServerTestCase):
    fixtures = ['initial.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(executable_path=r'D:\PyTechArt\topic7\Fins\chromedriver.exe')
        cls.selenium.implicitly_wait(60)

    def tearDown(self):
        self.selenium.close()
        super().tearDown()

    def test_login(self):
        # Login
        self.selenium.get(self.live_server_url+'/fins/login/')
        self.selenium.find_element_by_id("id_username").send_keys('anton')
        self.selenium.find_element_by_id("id_password").send_keys('1111')
        self.selenium.find_element_by_class_name('btn-success').click()

        # Main index
        self.selenium.get(self.live_server_url + '/fins/index/')
        self.selenium.find_element_by_class_name('selections').click()
        self.selenium.find_element_by_id('option_2').click()
        self.selenium.find_element_by_class_name('btn_select_shop').click()

        # Detail shop
        self.selenium.find_element_by_css_selector('input[value="Create new item"]').click()
        self.selenium.find_element_by_id('id_name').send_keys('Maksim')
        self.selenium.find_element_by_id('id_description').send_keys('BSTU 3 course 6 poit')
        self.selenium.find_element_by_id('id_comments').send_keys('Nice guy')
        self.selenium.find_element_by_id('id_price').send_keys(777.777)
        self.selenium.find_element_by_css_selector('input[value="Create"]').click()
        self.selenium.get('%s%s' % (self.live_server_url, '/fins/index/2/'))



