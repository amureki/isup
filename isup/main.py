from __future__ import unicode_literals

from argparse import ArgumentParser
import pkg_resources
import sys

import requests

COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'


def get_status(website):
    website_url = '{0}{1}.json'.format('http://isitup.org/', website)
    response = requests.get(website_url)
    data = response.json()
    return data.get('status_code', 0)


def main():
    parser = ArgumentParser(
        prog='isup',
        description='Simple console website status checker. '
                    'Just type: isup google.com')
    version = pkg_resources.require('isup')[0].version
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='isup {} using Python {}'.format(
            version, sys.version.split()[0]))

    parser.add_argument('website', help='website to check')

    known_args = parser.parse_args()
    if known_args.website:
        try:
            website = known_args.website.decode('utf-8')
        except AttributeError:
            website = known_args.website
        status = get_status(website)
        if status == 1:
            message = '{0}It\'s just you. ' \
                      '{1} is up.'.format(COLOR_GREEN, website)
        elif status == 2:
            message = '{0}It\'s not just you! ' \
                      '{1} looks down from here.'.format(COLOR_RED,
                                                         website)
        elif status == 3:
            message = '{0}Huh? {1} doesn\'t ' \
                      'look like a site.'.format(COLOR_RED, website)
        else:
            message = '{}isitup.org api error'.format(COLOR_RED)
        print(message)
    else:
        parser.print_usage()
