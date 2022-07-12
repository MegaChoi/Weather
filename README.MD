fucntional requirement 

get 
- temperature 
- cloud condition
- humidity 
- wind speed


TODO:
Find a way to deal with the tweet being duplicated 

LOG 
Client = tweepy.Client(
        consumer_key=consumer_key, 
        consumer_secret=consumer_secret,
        access_token=access_token, 
        access_token_secret=access_token_secret
)
for this peice of code to work, the part before each paramter is needed

12/7 
In the next Milestone, the bot must be able to operate on its own, that means it has to be able to post the weather of a random city in
the world 
- new library is used, Countryinfo, to determine the capital city of the ramdom chosed country from the pycountry country

1) read the json file of random country num code 
2) get the country name & alpha2 code from the country num code 
3) get the capital city name 
4) pass the city name and country name into the weather api 

* The bot is now can post weather of capital cities in the world every 5 mins

In the next Milestone, the bot must be able to reply to tweet requesting for weather info