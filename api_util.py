import urllib2
import json

global base_url
global auth_key
global ticket

# For authorization
def get_ticket(login_endpoint):
    url = base_url + login_endpoint
    headers = {"Content-Type": "application/json"}
    data = auth_key
    try:
        response = make_post_request(url, data, headers)
        return json.load(response).get("data").get("ticket")
    except urllib2.HTTPError as err:
        print("Failed to Login ")
        print(err.code)

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