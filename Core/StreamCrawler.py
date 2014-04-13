import twitter
import csv
import twitter__login
import json, time, sys, os

consumer_key = '2JRLM23QHyLyBABuqg4tqQ'
consumer_secret = 'avpoP356DDKbHtTRiicjKBC01yXqfaI8QCgfZebmjA'
access_token = '20692466-UHvKF9lGGyjhkyn1H5PX55nXdGbZsCmGOZo6Exaoy'
access_token_secret = 'FXEAFtjBvT9hRLxgPubBRUiv8sR7GTSpmVYoW9UArGLOi'
  
g_locations = "103.6271, 1.2427, 103.9993, 1.4548" #singapore 
g_language = "en"
g_geocode="1.3520830,103.8198360,80km"  #singapore radius

class StreamCrawler(object):
    def __init__(self):
        self.counter = 0
        self.fprefix = ""
        self.output  = None
        self.twitter_rest = twitter__login.login()
        self.twitter_stream = twitter.TwitterStream(auth=twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret))
        self.fname = None
        self.ufname = None
    
    def streamAPI(self):
        # By location only.
        resultSet = self.twitter_stream.statuses.filter(locations = g_locations)
        return resultSet
    
    def writeToFile(self, resultSet, aspect,keyword):
        if not os.path.isdir("data/"+aspect+"/"):
            os.mkdir("data/"+aspect+"/")
        if not os.path.isdir("data/"+aspect+"/user/"):
            os.mkdir("data/"+aspect+"/user/")
        self.fname = "data/"+aspect+"/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".json"
        self.ufname = "data/"+aspect+"/user/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".txt"
        i = 0
        j = 0
        outfile = open(self.fname, 'w')
        uoutfile = open(self.ufname, 'a')
        for r in resultSet:
            i+=1
            j+=1
            try:
                if len(r)>0 and r["place"]["country"]== "Singapore" and r["user"]["listed_count"] > 3: #strict filter
                    json.dump(r, outfile)
                    outfile.write("\n")
                    json.dump(r['user']['id'], uoutfile)
                    uoutfile.write("\n")
            except Exception as inst:
                print inst
                pass
            print i
            if(i>1000):
                outfile.close()
                uoutfile.close()
                self.fname = "data/"+aspect+"/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".json"
                self.ufname = "data/"+aspect+"/user/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".txt"
                outfile = open(self.fname, 'w')
                uoutfile = open(self.ufname, 'a')
                i = 0
                continue
            if (j>5000):
                return
        return
    
    def startStreamCrawling(self):
        rs = self.streamAPI()
        self.writeToFile(rs, "all-stream", "singapore")
        return
    
c = StreamCrawler()
c.startStreamCrawling()
    
    
    
    
    
    
    