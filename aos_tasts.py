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
        methods.TearDown()
