creds_path = 'C:/Users/ch328575/Documents/Projects/creds.json'
import json
import nltk, re, pprint
from pprint import pprint


import json
import os
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

import matplotlib.pyplot as plt
import numpy as np
import time

import numpy as np
import matplotlib.pyplot as plt

import tweepy
from tweepy import OAuthHandler


try:
    with open(creds_path) as creds_file:
        creds = json.load(creds_file)
except BaseException as e:
            print("Error on_data: %s" % str(e))        
        
consumer_key = creds["twitter_creds"]['consumer_key']
consumer_secret = creds["twitter_creds"]['consumer_secret']
access_token = creds["twitter_creds"]['access_token']
access_secret = creds["twitter_creds"]['access_secret']
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
print("ok")
from tweepy import Stream
from tweepy.streaming import StreamListener
import numpy as np
import matplotlib.pyplot as plt

class MyListener(StreamListener):
    anger_scores = np.array([0], dtype = np.float32)
    disgust_scores = np.array([0], dtype = np.float32)
    fear_scores = np.array([0], dtype = np.float32)
    joy_scores = np.array([0], dtype = np.float32)
    sadness_scores = np.array([0], dtype = np.float32)
    
    def on_data(self, data):
        try:
            with open('gervsmex.json', 'a') as f:    
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))        
        return True    
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#mexico', '#worldcup', "#germany", "germex"])