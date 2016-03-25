import requests
import datetime
import json

TEXTBELT_URL = 'http://textbelt.com/text'
ALERT_TEXT_TEMPLATE = 'ALERT: Page {} down as of {}'

def pageup(page, expected_statuses=[200], verify=False):
    """
    Check a given page to see if it's alive. Liveness is determined by the set
    of allowed numeric status codes passed by the user (only 200 by default).
    Verify determines whether or not SSL checking is enabled (disabled by
    default).
    """
    resp = requests.get(page, verify=verify)
    print("Got code %d" % resp.status_code)
    return resp.status_code in expected_statuses

def alert(text, number):
    post_body = {
        'message': text,
        'number': number
    }
    resp = requests.post(TEXTBELT_URL, data=post_body, verify=False)
    return resp.json()['success']

def alert_if_down(*pages, **kwargs):
    number = kwargs['number']
    allowed_codes = kwargs['allowed_codes']
    verify_ssl = kwargs.get('verify_ssl') or False
    for page in pages:
        print('Checking {}'.format(page))
        if not pageup(page, expected_statuses=allowed_codes, verify=verify_ssl):
            print('Alerting!')
            msg = ALERT_TEXT_TEMPLATE.format(page, datetime.datetime.utcnow())
            print(alert(msg, number))

