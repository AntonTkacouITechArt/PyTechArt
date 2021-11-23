from django.core.management import call_command
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.chrome.webdriver import WebDriver


class TestStatusCodePages(TestCase):
    """Test status code different pages """
    # multi_db = True
    fixtures = ['initial.json']


    def test_index_page(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_shop_detail_page(self):
        resp = self.client.get(reverse('shop_detail',args=(1,)))
        self.assertEqual(resp.status_code, 200)

    def test_shop_detail2_page(self):
        resp = self.client.get(reverse('shop_detail2',args=(1,)))
        self.assertEqual(resp.status_code, 200)

    def test_shop_update_page(self):
        resp = self.client.get('shop_update_page', args=(1,))
        self.assertEqual(resp.status_code, 200)

    def test_shop_delete_page(self):
        resp = self.client.get('shop_delete', args=(1,))
        self.assertEqual(resp.status_code, 200)

    def test_department_detail_page(self):
        resp = self.client.get('department_detail', kwargs={'shop_pk':1, 'pk':1})
        self.assertEqual(resp.status_code, 200)

    def test_department_create_page(self):
        resp = self.client.get(reverse('department_create', kwargs={'shop_pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_department_update_page(self):
        resp = self.client.get(reverse('department_update', kwargs={'shop_pk':1, 'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_department_delete_page(self):
        resp = self.client.get(reverse('department_delete', kwargs={'shop_pk':1, 'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_item_detail_page(self):
        resp = self.client.get(reverse('item_detail', kwargs={'shop_pk':1, 'dep_pk':1, 'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_item_create_page(self):
        resp = self.client.get(reverse('create_item_into_department', kwargs={'shop_pk':1, 'dep_pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_item_update_page(self):
        resp = self.client.get(reverse('update_item_into_department', kwargs={'shop_pk':1, 'dep_pk':1, 'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_item_delete_page(self):
        resp = self.client.get(reverse('delete_item_into_department', kwargs={'shop_pk':1, 'dep_pk':1, 'pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_login_page(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)

    def test_logout_page(self):
        resp = self.client.get(reverse('logout'))
        self.assertEqual(resp.status_code, 200)

    def test_filter_item_page(self):
        resp = self.client.get(reverse('filter_item', kwargs={'number':1}))
        self.assertEqual(resp.status_code, 200)

    def test_filter_shop_page(self):
        resp = self.client.get(reverse('filter_shop', kwargs={'number':1}))
        self.assertEqual(resp.status_code, 200)

    def test_compare_page(self):
        resp = self.client.get(reverse('compare_form', kwargs={'shop_pk':1}))
        self.assertEqual(resp.status_code, 200)

    def test_nogoods_page(self):
        resp = self.client.get(reverse('no_goods'))
        self.assertEquals(resp.status_code, 200)

    def test_unsold_items(self):
        resp = self.client.get(reverse('unsold_items'))
        self.assertEqual(resp.status_code, 200)


class TestAmountGoods(TestCase):
    """Test amount goods"""

    def setUp(self):
        call_command('clear_data', verbosity=0,)

    def test_amounts_goods_1(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('no_goods'))

    def test_amounts_goods_2(self):
        resp = self.client.get(reverse('shop_detail2', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('no_goods'))

    def test_amounts_goods_3(self):
        resp = self.client.get(reverse('department_detail', kwargs={'shop_pk':1,'pk':1}))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse('no_goods'))




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



