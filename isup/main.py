# coding=utf-8
import json
import sys
import urllib2

import config


def get_status(website):
    website_url = '{0}{1}.json'.format(config.ISITUP_API_URL, website)
    request = urllib2.Request(website_url, headers={u'User-Agent': config.USER_AGENT})
    response = urllib2.urlopen(request)
    data = json.load(response)
    return data.get(u'status_code', 0)


def main():
    if len(sys.argv) > 1:
        website = sys.argv[1].decode('utf-8')
        idna_website = website.encode('idna')
        status = get_status(idna_website)
        if status == 1:
            print(u'{0}It\'s just you. {1} is up.'.format(config.GOOD, website))
        elif status == 2:
            print(u'{0}It\'s not just you! {1} looks down from here.'.format(config.FAIL, website))
        elif status == 3:
            print(u'{0}Huh? {1} doesn\'t look like a site.'.format(config.FAIL, website))
        else:
            print(u'{}isitup.org api error'.format(config.FAIL))
    else:
        print(u'{}Please, enter website, for example: \nisup ya.ru'.format(config.WARNING))