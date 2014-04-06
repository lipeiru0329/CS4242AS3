import twitter
import csv
import twitter__login
import json, time, sys, os
'''
STREAM API Sample
'''
consumer_key = '2JRLM23QHyLyBABuqg4tqQ'
consumer_secret = 'avpoP356DDKbHtTRiicjKBC01yXqfaI8QCgfZebmjA'
access_token = '20692466-UHvKF9lGGyjhkyn1H5PX55nXdGbZsCmGOZo6Exaoy'
access_token_secret = 'FXEAFtjBvT9hRLxgPubBRUiv8sR7GTSpmVYoW9UArGLOi'
  
g_locations = "103.6271, 1.2427, 103.9993, 1.4548" #singapore 
g_language = "en"
g_geocode="1.3520830,103.8198360,100km"  #singapore radius

class StreamCrawler(object):
    def __init__(self):
        self.counter = 0
        self.fprefix = ""
        self.output  = None
        self.twitter_rest = twitter__login.login()
        self.twitter_stream = twitter.TwitterStream(auth=twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret))
    
    def streamAPI(self):
        # By location only.
        resultSet = self.twitter_stream.statuses.filter(locations = g_locations)
        return resultSet
    
    def writeToFile(self, resultSet, aspect,keyword):
        if not os.path.isdir("data/"+aspect+"/"):
            os.mkdir("data/"+aspect+"/")
        fname = "data/"+aspect+"/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".json"
        if os.path.isfile(fname):
            fname = "data/"+aspect+"/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".json"
        f = open(fname,'w')
        i = 0
        for r in resultSet:
            i+=1
            f.write(str(r)+"\n")
            print i
            if(i>200):
                f.close()
                return
        f.close()
        return
    
    def startStreamCrawling(self):
        rs = self.streamAPI()
        self.writeToFile(rs, "all-stream", "singapore")
        return
    
c = StreamCrawler()
c.startStreamCrawling()
    
    
    
    
    
    
    