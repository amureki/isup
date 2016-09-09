# coding: utf-8
from unittest import TestCase

from isup.cli import main as isup_main, get_status, strip_scheme


class TestMain(TestCase):
    WEBSITES = ['http://google.com', 'ya.ru', u'кто.рф']

    def test_main(self):
        self.assertEqual(isup_main([None]), 0)

    def test_get_status(self):
        for website in self.WEBSITES:
            status = get_status(website)
            self.assertEqual(status, 1)

    def test_strip_scheme(self):
        for website in self.WEBSITES:
            cleaned_website = strip_scheme(website)
            self.assertIn(cleaned_website, website)
            self.assertNotIn(cleaned_website, 'http')
