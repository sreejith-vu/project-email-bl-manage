#/usr/bin/env python
#Individual func to remove from blacklist

import requests

WORKFLOW_URL_1 = 'XXX'
MAILGUN_URL_1 = 'XXX'
MAILGUN_URL_2 = 'XXX'
WORKFLOW_HEADERS = {'Authorization': 'Basic XXX'}
MAILGUN_HEADERS = {'Authorization': 'Basic XXX'}

def email_whitelist(URL, HEADERS):
    try:
        print "Removing email from Blacklist"
        response = requests.delete(URL, headers=HEADERS, timeout=15)
        if response.status_code == 200:
            return 0
        else:
            return 1
    except Exception as error:
        return "Unable to resolve the URL while whitelisting, got the error %s" % error

def workflow_b(email):
    CHECK_URL = WORKFLOW_URL_1 + email
    return email_whitelist(CHECK_URL, WORKFLOW_HEADERS )

def mailgun_b(email):
    CHECK_URL = MAILGUN_URL_1 + email
    return email_whitelist(CHECK_URL, MAILGUN_HEADERS )

def mailgun_c(email):
    CHECK_URL = MAILGUN_URL_2 + email
    return email_whitelist(CHECK_URL, MAILGUN_HEADERS )
