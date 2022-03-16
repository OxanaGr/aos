import unittest
import aos_methods as methods


class aosPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_crtnwacnt():
        methods.SetUp()
        methods.create_new_del_account()
        methods.log_out()
        methods.login()
        methods.checkout_shopping_cart()
        methods.log_out()
        methods.checking_homepage_texts()
        methods.check_contact_us()
        methods.links_top_nav_menu_and_logo()
        methods.check_social_media_links()
        methods.login()
        methods.my_order()
        methods.del_account()
        methods.TearDown()