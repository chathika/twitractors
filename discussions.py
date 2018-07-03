import json
import sys
'''could we get discussions extracted from the raw data.
Something like a csv file where there's a column for discussion id, individual, and tweet text response?'''
fileName = sys.argv[1]
tweets = []
ids = []

import simplejson

with open(fileName) as f:
    try:
        z = simplejson.load(f)
        print(str(len(z)))
    except ValueError as e:
        print('Error parsing JSON:', str(e))

# with open (fileName) as f:
#       json.loads(f)
#d = json.loads(open(fileName, 'r'))
# with open('clean.json', 'w') as outfile:
#     json.dump(tweets, outfile)
#     for line in f:
#         # check for nulls
#         if "id_str" in line:
#             ids.append(json.loads(line)["id_str"])
#         if "in_reply_to_user_id_str" in line:
#             tweets.append(json.loads(line)["in_reply_to_user_id_str"])
# #         #if "retweeted_status" in line:
#
# print(str(len(ids)))
# print(str(len(tweets)))
# for id in ids:
#     if id in tweets:
#         print(id)
# with open (fileName) as f:
#     for line in f:
#         tweets.append(json.loads(line))
# with open(file, 'w') as f:
#     json.dump(tweets, f)
#json_val = json.load(open(fileName))
# with open('clean.json', 'w') as outfile:
#     json.dump(tweets, outfile)

            # Because id is int64 there's a string implementation that much more usable, field is not null
            # users_who_tweet.append(json.loads(line)["retweeted_status"])
            #print(json.loads(line)["retweeted_status"]["user"]["id_str"])
            #print(json.loads(line)["user"]["id_str"])
#for tweet in tweets:
# for k, v in ids.iteritems():
#     print()

#with open(sys.argv[1]) as f:
#    data = json.loads(f)
#pprint(data['twitter'][0])