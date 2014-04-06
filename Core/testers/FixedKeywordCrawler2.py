import tweepy
from tweepy import StreamListener
import json, time, sys


consumer_key = '2JRLM23QHyLyBABuqg4tqQ'
consumer_secret = 'avpoP356DDKbHtTRiicjKBC01yXqfaI8QCgfZebmjA'
access_token = '20692466-4kkQfaO8V0e2cVBDzfYg4EkFdQO9u0CNZLoP8Xma5'
access_token_secret = '0bUGan28R0Dt2f0NIIjA2AcCkNUelANx674aWUH9Oj08f'

class FixedKeywordCrawler2():
    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    def stream(self):
        '''
        l = StdOutListener()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = tweepy.Stream(auth, l)
        stream.filter(track=['Singapore'])
        '''
        track  = ["soccer, football, singapore"]
        locations = [103.61,1.22,104.01356,1.456674]
        language = ['en']
        follow = []
        listen = SListener(api, 'test')
        stream = tweepy.Stream(auth, listen)
        print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))
        try: 
            stream.filter(track = track, follow = follow, locations = locations)
        except:
            print "error!"
            stream.disconnect()
