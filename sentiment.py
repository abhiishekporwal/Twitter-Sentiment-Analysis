
import tweepy
from textblob import TextBlob
import csv
import re
import sys
import pandas as pd

consumer_key='L0WaHBxtMOS9sZc05o3tBx2Tq'
consumer_secret='kUOhJE0S9CUKrJie1FMKuDP7iE2Q9k23julRg9dpeqI0tbmNpL'

access_token_key='985801184211386368-ibpWk0slO4JnfRxWdFNQZ6K0VRU81YC'
access_token_secret='zvsPqflwI4Shs8Z95VFv6PyStq6bwhq853Vw7CzoHFxmU'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)
topicname='Avengers'
pubic_tweets=api.search(topicname)
unwanted_words=['@','RT',':','https','http']
symbols=['@','#']
data=[]
for tweet in pubic_tweets:
    text=tweet.text
    textWords=text.split()
    #print (textWords)
    cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
    print (cleanedTweet)
    #print (TextBlob(cleanedTweet).tags)
    analysis= TextBlob(cleanedTweet)
    print (analysis.sentiment)
    polarity = 'Positive'
    if(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    if(0<=analysis.sentiment.polarity <=0.2):
        polarity = 'Neutral'
    print (polarity)
    dic={}
    dic['Sentiment']=polarity
    dic['Tweet']=cleanedTweet
    data.append(dic)
df=pd.DataFrame(data)
df.to_csv('C:\\Users\\Dell\\Desktop\\analysis5.csv')