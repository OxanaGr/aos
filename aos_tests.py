import unittest
import aos_methods as methods


class aosPositiveTestCases(unittest.TestCase):
    @staticmethod
    def test_CrtNwAcnt():
        methods.SetUp()
        methods.CrtNwAcnt()
        methods.log_out()
        methods.Login()
        methods.log_out()
        methods.Checking_homepage_texts()
        methods.links_top_nav_menu_and_logo()
        methods.Check_CONTACT_US()
        methods.Check_Social_Media_links()
        methods.Login()
        methods.My_Order()
        methods.Del_Acnt()
        methods.TearDown()