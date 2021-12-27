#!/usr/bin/env python3

import requests
# from requests_oauthlib import OAuth1

# client_key = '...'
# client_secret = '...'

# request_token_url = 'https://api.twitter.com/oauth/request_token'
# oauth = OAuth1Session(client_key, client_secret=client_secret)
# resource_owner_key = fetch_response.get('oauth_token')
# resource_owner_secret = fetch_response.get('oauth_token_secret')

# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

# requests.get(url, auth=auth)

if __name__ == "__main__":
    response = requests.get("https://adventofcode.com/2021/day/1/input")
    print(response.text)
