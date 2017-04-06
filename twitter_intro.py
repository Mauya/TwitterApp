import json
import tweepy
from tweepy import OAuthHandler
CONSUMER_KEY = 'NN8926PXRjwnJxUMLB6f2tclB'
CONSUMER_SECRET = 'JUtAJIQvFZZxWpdoSlduhsbXJ8Z6T576heidjvEfDucqjbZC1z'
OAUTH_TOKEN = '38696744-BWJZSIptjIA92x90lHngqZ96EPASQ7PVpBx791Z7H'
OAUTH_TOKEN_SECRET = '5Nuau0xiyNuVdpDuLZifWJapjli33OKSf8gDIETpQXuqA'
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)
DUB_WOE_ID = 560743
LON_WOE_ID = 44418
dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
print json.dumps(dub_trends, indent=1)
print json.dumps(lon_trends, indent=1)
