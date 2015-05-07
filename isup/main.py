import sys
import urllib2
from urlparse import urlparse


WEBSITE_IS_DOWN = 0
WEBSITE_IS_UP = 1
SERVICE_ERROR = 2
NOT_WEBSITE = 3

GOOD = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDLINE = '\033[0m'


def website_status(website):
    url = urlparse(website).geturl()

    is_up_url = u'http://isup.me/{}'.format(url)
    try:
        response = urllib2.urlopen(is_up_url)
    except:
        return SERVICE_ERROR
    if response.getcode() != 200:
        return SERVICE_ERROR

    html = response.read()
    if u'doesn\'t look like a site' in html:
        return NOT_WEBSITE
    if u'looks down' in html:
        return WEBSITE_IS_DOWN
    return WEBSITE_IS_UP


def main():
    if len(sys.argv) > 1:
        website = sys.argv[1]
        status = website_status(website)
        if status == WEBSITE_IS_UP:
            print(u'{0}It\'s just you. {1} is up.'.format(GOOD, website))
        elif status == WEBSITE_IS_DOWN:
            print(u'{0}It\'s not just you! {1} looks down from here.'.format(FAIL, website))
        elif status == NOT_WEBSITE:
            print(u'{0}Huh? {1} doesn\'t look like a site on the interwho.'.format(FAIL, website))
        else:
            print(u'{}isup.me error'.format(FAIL))
    else:
        print(u'{}Please, enter website, for example: \nisup ya.ru'.format(WARNING))