import json
import sys
from collections import Counter

'''

Created on June 19, 2018

@author: Laura Mann

Aggregates the file into a set by user and counts the number of times tweeted during the match.
:TODO should maybe write to something else other then the file system because the results have to be read into
a list which is annoying.


'''
fileName = sys.argv[1]
users_who_tweet = []

with open (fileName) as f:
    for line in f:
        if "user" in line:
            # Because id is int64 there's a string implementation that much more usable, field is not null
            users_who_tweet.append(json.loads(line)["user"]["id_str"])

if not users_who_tweet:
    print("Something went wrong the list is empty")
else:
    print("The total length is " + str(len(users_who_tweet)))
    users = Counter(users_who_tweet)
    print("Unique Users" + str(len(set(users))))
    print(users.most_common(10))
    print(str(len({k:v for (k,v) in users.items() if v > 1})))
#file_out = open("user_analytics.csv", "a+")
#file_out.write("time,polarity,subjectivity\n")
#for tweet_text in tweet_texts:
