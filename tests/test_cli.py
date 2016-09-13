# coding: utf-8
from unittest import TestCase

from isup.cli import main as isup_main, get_status, parse_domain


class TestMain(TestCase):
    GOOD_URLS = [
        'http://google.com',
        'https://www.bing.com/',
        'https://www.amazon.com/robots.txt',
        'ya.ru',
        u'кто.рф',
    ]

    BAD_URLS = [
        'dummy',
        'comma,test',
    ]

    def test_main(self):
        self.assertEqual(isup_main([None]), 0)

    def test_get_status_ok(self):
        for url in self.GOOD_URLS:
            status = get_status(url)
            self.assertEqual(status, 1)

    def test_get_status_fail(self):
        for url in self.BAD_URLS:
            status = get_status(url)
            self.assertEqual(status, 3)

    def test_parse_domain(self):
        for url in self.GOOD_URLS:
            cleaned_website = parse_domain(url)
            self.assertIn(cleaned_website, url)
            self.assertNotIn(cleaned_website, 'http')
