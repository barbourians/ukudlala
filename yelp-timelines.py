# http://matatat.org/yelp-timelines.html

import json
import urllib2

import oauth2

# Use your own keys here
TOKEN = None
TOKEN_SECRET = None
CONSUMER = None
CONSUMER_SECRET = None

# This function performs a Yelp API request, taken from Yelp's python example
def api_request(url, url_params):
    """ Make a request with Yelp's API """
    consumer = oauth2.Consumer(CONSUMER, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)

    oauth_request = oauth2.Request(method="GET", url=url, 
                                   parameters=url_params)
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': TOKEN,
                          'oauth_consumer_key': CONSUMER})

    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), 
                               consumer, token)
    signed_url = oauth_request.to_url()

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response


def search(term, location, limit=5):
    """ Search Yelp with a term and location """
    url = 'http://api.yelp.com/v2/search'
    url_params = {'term': term.replace(' ', '+'),
                  'location': location.replace(' ', '+'),
                  'limit': limit}
    response = api_request(url, url_params)
    bizs = response['businesses']
    return bizs

from pprint import pprint
bizs = search('sushi', 'Mission, San Francisco, CA')
# Look at our results and the ratings
pprint([(biz['name'], biz['rating']) for biz in bizs])


def get_business(biz_id):
    """ Get business data from Yelp """
    url = 'http://api.yelp.com/v2/business/{}'.format(biz_id)
    response = api_request(url, None)
    return response





print ''
print 'EOF'
# EOF