import json 
import pycountry
from countryinfo import CountryInfo 
import random
import time
import requests
import tweepy

consumer_key = 'Sw0EPH1KUKT8hR6AcsRa6aO5c'
consumer_secret = 'Bd5KHMfSeZ8EWXI5AMC3rcFSkP9oMJTNIX1h8Rq1LZnuujfnck'
access_token = '1544648798089072641-UUBqCSAPnpgS5nd2WRT7iatmAGl9Y0'
access_token_secret = '8JE8MjCyOZoSjrS511wtQoV6gZMAqQc6irWz6FwHVGuRH'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKQXegEAAAAAII9lyNxt04yfv46Jvtx%2B%2BdmK%2FRU%3DO2e9ku0c8m1clQ6NG9VBgL0c6Uk2TdJ8QypnaCFcjZJxr8QUo6'


#authentication 
auth = tweepy.OAuth1UserHandler(
consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)

#client idk wtf this does but it works 
Client = tweepy.Client(
consumer_key=consumer_key, 
consumer_secret=consumer_secret,
access_token=access_token, 
access_token_secret=access_token_secret
)
request_line = "what the weather like at"
latest_mention_id = 1
test = api.mentions_timeline(since_id= latest_mention_id)
#only find the mentions that has ids greater than the latest mention.id
for mention in test:
    print("Mention tweet found")
    print(f"{mention.author.screen_name} - {mention.text}")
    print (mention.id)
    latest_mention_id = mention.id

    #check if the tweet is not a reply to another tweet
    if mention.in_reply_to_status_id is None:
        if request_line in mention.text.lower():
            print("Attempting to reply")
            print(mention.text)
            