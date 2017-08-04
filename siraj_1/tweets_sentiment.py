import tweepy
from textblob import TextBlob

key = '8nNoyr59oY3Haf61qCTEsnNcT'
secret = 'q8XgKflxIcumI2PdcwzyrFutEzIGjPMt1dc6CJxmfRWU0Y21yp'

token = '77358424-BvMMdu9E7qluVFEhiMIXBg8BtL1tU0Pefc0oGc2BR'
secret_token = 'CBE0KvgD9vcKD2Q8ZenWwAZFVTmQbfco4oJXAjjAW9V84'

auth = tweepy.OAuthHandler(key,secret)
auth.set_access_token(token,secret_token)

api = tweepy.API(auth)

public_tweets = api.search('Froome')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

