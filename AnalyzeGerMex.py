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
#from mtranslate import translate
from multiprocessing import Pool
import traceback
import boto3
from langdetect import detect
import string
import os.path
import time

def clean_tweet( tweet):
    cleanString = re.sub('\n',' ', tweet )
    cleanString = re.sub('\r',' ', cleanString )
    cleanString = re.sub(',',' ', cleanString )
    return cleanString
def translateChunk(data):
    GerMexTweetsChunk = pd.DataFrame(data) 
    tweet_texts = GerMexTweetsChunk.text
    #print(tweet_texts)
    translate = boto3.client(service_name="translate", use_ssl=True)
    def tryTranslate(t):
        text = t
        try:
            printable = set(string.printable)
            text = clean_tweet(text)
            text = "".join(filter(lambda x: x in printable, text))
            language = detect(text)
            translated = translate.translate_text(Text=text, SourceLanguageCode=language, TargetLanguageCode="en").get("TranslatedText") 
            time.sleep(0.5)
            return translated
        except Exception:
            traceback.print_exc()
            return text
    tweet_texts = tweet_texts.apply(lambda t:tryTranslate(t))
    GerMexTweetsChunk.text = tweet_texts
    #print(GerMexTweetsChunk.text)
    header_required = False
    if os.path.isfile("chunk.csv"):
        header_required = True
    with open('chunk.csv', 'a') as f:
        GerMexTweetsChunk.to_csv(f, header=header_required, encoding='utf-8')
    print(GerMexTweetsChunk.text)
    #GerMexTweetsChunk.text = GerMexTweetsChunk.text.apply(lambda t: translate(str(t), "en", "auto"))
    #print(GerMexTweetsChunk.head())
    #time.sleep(1)
    return GerMexTweetsChunk

if __name__ == '__main__':

    fileName = "gervsmex.json"

    def json_readr(file):
        print(file)
        returnval = []
        for line in open(file, mode="r"):
            if "{\"created_at\"" in line:
                returnval.append(json.loads(line))
            #yield json.loads(line['text'])
        return returnval
    tweets = json_readr(fileName)
    GerMexTweets=json_normalize(tweets)
    print("Main sending data to workers")
    pool = Pool()
    pool.map(translateChunk,np.array_split(GerMexTweets,1000))
    #translateChunk(GerMexTweets)
    print("Workers are done")
    #result = pd.DataFrame(result)        
    #result.to_csv("GerMexTweetsTranslated.csv")
    #print(result.head())
    #!pip install langdetect
    #!pip install mtranslate

    
