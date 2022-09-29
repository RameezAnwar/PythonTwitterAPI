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




#test if api connection is working
public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)



#checking panda functionality
columns = ['Time', 'User', 'Tweet']
data = []
for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

#print(data)

#adding tweets to dataframe to be saveable
df = pd.DataFrame(data, columns = columns)
#print(df)

#saving tweets to csv file
df.to_csv( 'tweets.csv')


###########################################################################################

#getting tweets from specific user
user = 'veritasium'
limit = 300

#tweepy method of bypassing twitter 200 limit
tweets = tweepy.Cursor(api.user_timeline,  screen_name = user, 
count = 200, tweet_mode = 'extended').items(limit)

#without using limit bypass
#tweets = api.user_timeline(screen_name = user,count = limit, tweet_mode = 'extended' )

#for tweet in tweets:
#    print( tweet.full_text)


#saving user tweets to dataframe and saving it
user_columns = ['User', 'Tweet']
user_data = []

for tweet in tweets:
    user_data.append([tweet.user.screen_name, tweet.full_text])

user_df = pd.DataFrame(user_data, columns = user_columns)

#print(user_df)
user_df.to_csv( 'user_tweets.csv')


#####################################################################################


