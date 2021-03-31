import tweepy as tw
import pandas as pd
import json

#lendo o arquivo que contem os dados de autenticação
file_json = open('twitter_tokens.json','r')
parsed_json = json.load(file_json)

consumer_key = parsed_json['api_key']
consumer_secret = parsed_json['api_key_secret']
access_token = parsed_json['access_token']
access_token_secret = parsed_json['access_token_secret']


auth = tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tw.API(auth)

public_tweets = api.home_timeline()

query_search = '#ENEM' + "-filter:retweets"

cursor_tweets = tw.Cursor(api.search,
            q=query_search).items(10)

tweets = tw.Cursor(api.search,
            q=query_search).items(100)

for tweet in public_tweets:
    print(tweet.created_at)
    print(tweet.text)
    print(tweet._json)

twkeys = tweet._json.keys()
print(twkeys)

tweets_dict = {}
tweets_dict = tweets_dict.fromkeys(twkeys)

print(tweets_dict)

query_search = '#ENEM' + "-filter:retweets"
cursor_tweets = tw.Cursor(api.search,
            q=query_search).items(100)

for tweet in cursor_tweets:
    for key in tweets_dict.keys():
        try:
            twkey = tweet._json[key]
            tweets_dict[key].append(twkey)
        
        except:
            tweets_dict[key] = [twkey]
        print('twets_dict[key]: {} - tweet[key]: {}'.format(tweets_dict[key], twkey))

dfTweets = pd.DataFrame.from_dict(tweets_dict)
# print(dfTweets.head())
print(dfTweets.text)