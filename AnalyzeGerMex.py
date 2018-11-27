import json 
from pprint import pprint
import sys
import re
import numpy as np
import pandas as pd
import unicodedata
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
from pandas.io.json import json_normalize
from mtranslate import translate
from multiprocessing import Pool

def translateChunk(data):
    GerMexTweetsChunk = pd.DataFrame(data) 
    tweet_texts = GerMexTweetsChunk.text
    def tryTranslate(t):
        try:
            return translate(str(t), "en", "auto") 
        except:
            return t
    tweet_texts = tweet_texts.apply(lambda t: tryTranslate(t))
    """for idx, tweet_text in tweet_texts.iteritems():
        tweet_texts.set_value(idx, translate(str(tweet_text), "en", "auto"))"""
    GerMexTweetsChunk.text = tweet_texts
    with open('chunk.csv', 'a') as f:
        GerMexTweetsChunk.to_csv(f)
    print(GerMexTweetsChunk.text)
    #GerMexTweetsChunk.text = GerMexTweetsChunk.text.apply(lambda t: translate(str(t), "en", "auto"))
    #print(GerMexTweetsChunk.head())
    return GerMexTweetsChunk

if __name__ == '__main__':

    fileName = "gervsmex.json"

    def json_readr(file):
        print(file)
        returnval = []
        for line in open(file, mode="r"):
            if "{" in line:
                returnval.append(json.loads(line))
            #yield json.loads(line['text'])
        return returnval
    tweets = json_readr(fileName)
    GerMexTweets=json_normalize(tweets)
    print("Main sending data to workers")
    with Pool(processes=6) as pool:
        result = pd.DataFrame(pool.map(translateChunk,np.array_split(GerMexTweets,6)))
        print("Workers are done")
        result = pd.DataFrame(result)        
        result.to_csv("GerMexTweetsTranslated.csv")
        print(result.head())
    #!pip install langdetect
    #!pip install mtranslate

    