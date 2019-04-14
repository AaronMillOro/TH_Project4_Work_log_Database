import unittest
import sqlite3

from tools import *


class SearchTest(unittest.TestCase):

    def SetUp(Self):
        pass

    def test_search_employee_false(self):
        """Search a non-present entry in db"""
        search_name = "Mila Kunis"
        data = [(
                "Adrew Ryan","SAV","2017-02-23 00:00:00",60,
                "Post-achat"
                )]
        expected = search_employee(search_name)
        self.assertNotEqual(expected, data)

    def test_search_employee_true(self):
        """Search a present unique entry"""
        search_name = "Sylverster Stalin"
        data = [(
                "Sylverster Stalin",
                "Disposition of new project on GitHub",
                "2012-02-24 00:00:00",
                200,"Internal application to receive updates"
                )]
        expected = search_employee(search_name)
        self.assertEqual(expected, data)

    def test_search_time_true(self):
        """Search a present unique entry"""
        s_time = 200
        data = [(
                "Sylverster Stalin",
                "Disposition of new project on GitHub",
                "2012-02-24 00:00:00",
                200,"Internal application to receive updates"
                )]
        expected = search_time(s_time)
        self.assertEqual(expected, data)

    def test_search_string_true(self):
        """Search a present entry by keyword en task name or notes"""
        keyword = "Pesquisa"
        data = [(
                "John Lenin",
                "Pesquisa do mercado local",
                "2011-02-02 00:00:00",
                2000,"Pesquisa no internet"
                )]
        expected = search_string(keyword)
        self.assertEqual(expected, data)

    def test_search_date_true(self):
        """ Search a specific date"""
        date_to_search = "2019-03-13 00:00:00"
        data = [(
                "Guisseppe Ottaviani",
                "Release of new record 2019",
                "2019-03-13 00:00:00",
                4,"ASOT"
                )]
        expected = search_date(date_to_search)
        self.assertEqual(expected, data)


if __name__ == '__main__':
    unittest.main()
