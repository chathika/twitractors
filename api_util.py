import urllib2
import json
import sys
import tweepy
from tweepy import OAuthHandler

global base_url
global auth_key
global ticket

# # For token authorization
# def get_ticket(login_endpoint):
#     url = base_url + login_endpoint
#     headers = {"Content-Type": "application/json"}
#     data = auth_key
#     try:
#         response = make_post_request(url, data, headers)
#         return json.load(response).get("data").get("ticket")
#     except urllib2.HTTPError as err:
#         print("Failed to Login ")
#         print(err.code)
#
# def get_auth(cred_path):
#     try:
#         with open(cred_path) as creds_file:
#             auth_key = json.load(creds_file)
#     except BaseException as e:
#         return: "Error on_data: %s" % str(e)
#     consumer_key = auth_key["twitter_creds"]['consumer_key']
#     consumer_secret = auth_key["twitter_creds"]['consumer_secret']
#     access_token = auth_key["twitter_creds"]['access_token']
#     access_secret = auth_key["twitter_creds"]['access_secret']
#
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
#
# api = tweepy.API(auth)

# A simple get method
def make_request(url, headers):
    request = urllib2.Request(url)
    for key, value in headers.items():
        request.add_header(key, value)
    return urllib2.urlopen(request)

# A simple post method
def make_post_request(url, data, headers):
    request = urllib2.Request(url)
    for key, value in headers.items():
        request.add_header(key, value)
    return urllib2.urlopen(request, json.dumps(data))

# Read file