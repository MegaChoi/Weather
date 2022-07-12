import tweepy

class Tweet:
    
    def __init__(self ,city_name, temperature, clouds, humidity, wind) -> None:
        self.city_name = city_name
        self.temperature = temperature
        self.clouds = clouds
        self.humidity = humidity
        self.wind = wind

    def postTweet(country_name, city_name, temperature, clouds, humidity, wind):
        #Twitter tokens
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
        weather_tweet = (city_name + " - " + country_name + 2*"\n" + temperature + "\n" + humidity + "\n" + clouds  + "\n" + wind)
        new_weather_tweet = Client.create_tweet(text= weather_tweet)
