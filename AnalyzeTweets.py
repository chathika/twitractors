import json 
from pprint import pprint
import sys
from textblob import TextBlob
import re
import numpy
import pandas
fileName = sys.argv[1]
tweet_texts = []
count = 0
with open (fileName) as f:
    for line in f:
        if "created_at" in line:
            count = count + 1
            tweet_texts.append((json.loads(line)["created_at"],json.loads(line)["text"]))
print(count)

def clean_tweet( tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

file_out = open("sentiment_timeseries.csv", "a+")
file_out.write("time,polarity,subjectivity\n")
for tweet_text in tweet_texts:
    analysis = TextBlob(clean_tweet(tweet_text[1]))
    tweet_sentiment = str(tweet_text[0]) + "," + str(analysis.sentiment.polarity) + "," + str(analysis.sentiment.subjectivity) + "\n"
    #print(tweet_sentiment)
    file_out.write(tweet_sentiment)
