#/usr/bin/env python
#Individual func to check blacklist

import requests

WORKFLOW_INFO = 'XXX'
MAILGUN_INFO_1 = 'XXX'
MAILGUN_INFO_2 = 'XXX'
WORKFLOW_HEADERS = {'Authorization': 'Basic XXX'}
WORKFLOW_URL_1 = 'XXX'
MAILGUN_URL_1 = 'XXX'
MAILGUN_URL_2 = 'XXX'
MAILGUN_HEADERS = {'Authorization': 'Basic XXX'}

def provider_check(INFO):
    if INFO == WORKFLOW_INFO:
        return 1
    elif INFO == MAILGUN_INFO_1:
        return 2
    elif INFO == MAILGUN_INFO_2:
        return 3

def email_blacklist_check(INFO, STATUS_CODE):
    print "Checking in %s." % INFO
    if STATUS_CODE == 200:
        print "Blacklisted on %s" % (INFO)
        return provider_check(INFO)
    elif STATUS_CODE == 404:
        print "Not blacklisted"
        return 0
    else:
        print "Response received is: ", STATUS_CODE 


def http_check(INFO, URL, HEADERS):
    try:
        response = requests.get(URL, headers=HEADERS, timeout=15)
        STATUS_CODE = response.status_code
        return email_blacklist_check(INFO, STATUS_CODE)
    except Exception as error:
        return "Unable to resolve the URL, got the error %s" % error

def workflow_b(email):
    CHECK_URL = WORKFLOW_URL_1 + email
    return http_check(WORKFLOW_INFO, CHECK_URL, WORKFLOW_HEADERS )

def mailgun_b(email):
    CHECK_URL = MAILGUN_URL_1 + email
    return http_check(MAILGUN_INFO_1, CHECK_URL, MAILGUN_HEADERS )

def mailgun_c(email):
    CHECK_URL = MAILGUN_URL_2 + email
    return http_check(MAILGUN_INFO_2, CHECK_URL, MAILGUN_HEADERS )
