from __future__ import unicode_literals

from argparse import ArgumentParser

try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import requests

from . import __version__

COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'


def parse_domain(url):
    if not url.startswith('http'):
        url = 'http://{0}'.format(url)
    parsed_uri = urlparse(url)
    return '{uri.netloc}'.format(uri=parsed_uri)


def get_status(url):
    cleaned_url = parse_domain(url)
    api_url = 'http://isitup.org/{0}.json'.format(cleaned_url)
    try:
        response = requests.get(api_url)
        data = response.json()
        return data.get('status_code', 0)
    except requests.exceptions.ConnectionError:
        return 4


parser = ArgumentParser(
    prog='isup',
    description='Simple console website status checker. '
                'Just type: isup google.com'
)

parser.add_argument(
    '-v', '--version',
    action='version',
    version='isup {0}'.format(__version__))
parser.add_argument('website', help='website to check')


def main(cli_args=None):
    if cli_args is not None:
        known_args = parser.parse_args(cli_args)
    else:
        known_args = parser.parse_args()

    if known_args.website:
        try:
            website = known_args.website.decode('utf-8')
        except AttributeError:
            website = known_args.website

        status = get_status(website)
        if status == 1:
            message = '{0} It\'s just you. ' \
                      '{1} is up.'.format(COLOR_GREEN, website)
        elif status == 2:
            message = '{0} It\'s not just you! ' \
                      '{1} looks down from here.'.format(COLOR_RED,
                                                         website)
        elif status == 3:
            message = '{0} Huh? {1} doesn\'t ' \
                      'look like a site.'.format(COLOR_RED, website)
        elif status == 4:
            message = '{0} Please check your network connection. ' \
                      'Seems like we\'re offline'.format(COLOR_RED)
        else:
            message = '{0}isitup.org api error'.format(COLOR_RED)
        print(message)
        return 0
    else:
        parser.print_usage()
        return 0


if __name__ == '__main__':
    exit(main())
