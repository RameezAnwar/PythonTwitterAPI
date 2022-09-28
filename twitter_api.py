import tweepy
import configparser
import pandas as pd


#get credentials

config = configparser.ConfigParser()
config.read('config.ini')


api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#check if config file working
#print(api_key)

#get aunthentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()

#test if api connection is working
#for tweet in public_tweets:
#    print(tweet.text)

columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

#print(data)

#adding tweet to dataframe to be saveable
df = pd.DataFrame(data, columns = columns)
#print(df)

df.to_csv( 'tweets.csv')


