import json 
from pprint import pprint
import sys
from textblob import TextBlob
import re
import numpy
import pandas
import unicodedata
fileName = sys.argv[1]
tweet_texts = []
count = 0
with open (fileName) as f:
    for line in f:
        if "created_at" in line and "location" in line and "lang" in line:
            count = count + 1
            tweet_texts.append((json.loads(line)["created_at"],json.loads(line)["text"],json.loads(line)["user"]["location"],json.loads(line)["user"]["lang"]))
print(count)

def clean_tweet( tweet):
    cleanString = re.sub('\W+',' ', tweet )
    return cleanString
    #return ' '.join(re.sub("(#@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
'''
file_out = open("sentiment_timeseries.csv", "w+")
file_out.write("time,polarity,subjectivity\n")
for tweet_text in tweet_texts:
    analysis = TextBlob(clean_tweet(tweet_text[1]))
    tweet_sentiment = str(tweet_text[0]) + "," + str(analysis.sentiment.polarity) + "," + str(analysis.sentiment.subjectivity) + "\n"
    #print(tweet_sentiment)
    file_out.write(tweet_sentiment)
'''
file_out = open("text_location_timeseries.csv", "w+")
file_out.write("time,text,location\n")
for tweet_text in tweet_texts:
    if tweet_text[1] != None:
        text = clean_tweet(unicode(tweet_text[1].encode("utf-8"), errors='ignore') )
    if tweet_text[2] != None: 
        location = clean_tweet(unicode(tweet_text[2].encode("utf-8"), errors='ignore') )
    if tweet_text[3] != None: 
        lang = clean_tweet(unicode(tweet_text[3].encode("utf-8"), errors='ignore') )
    tweet_location = tweet_text[0] + "," + text  + "," + location  + "," + lang + "\n"
    #print(tweet_location)
    file_out.write(tweet_location)

