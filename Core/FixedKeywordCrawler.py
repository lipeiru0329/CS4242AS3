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

class FixedKeywordCrawler(object):
    def __init__(self):
        self.counter = 0
        self.fprefix = ""
        self.output  = None
        self.twitter_rest = twitter__login.login()
        self.twitter_stream = twitter.TwitterStream(auth=twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret))
    
    def searchAPI(self, keywords, expectedNumberofResults):
        resultSet = self.twitter_rest.search.tweets(q=keywords, geocode = g_geocode, count = expectedNumberofResults, language = g_language)
        return resultSet['statuses']
    
    def writeToFile(self, resultSet, aspect,keyword):
        if not os.path.isdir("data/"+aspect+"/"):
            os.mkdir("data/"+aspect+"/")
        if not os.path.isdir("data/"+aspect+"/user/"):
            os.mkdir("data/"+aspect+"/user/")
        fname = "data/"+aspect+"/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".json"
        ufname = "data/"+aspect+"/user/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".txt"
        #if os.path.isfile(fname):
         #   fname = "data/"+aspect+"/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".json"
          #  ufname = "data/"+aspect+"/user/"+keyword+"-"+time.strftime('%Y%m%d-%H%M%S')+".txt"
        outfile = open(fname, 'w')
        uoutfile = open(ufname, 'w')
        for r in resultSet:
            if r["metadata"]["iso_language_code"] == "en" and r["user"]["listed_count"] > 3:
                json.dump(r, outfile)
                outfile.write("\n")
                json.dump(r['user']['id'], uoutfile)
                uoutfile.write("\n")
        outfile.close()
        uoutfile.close()
        return
    
    def searchSoccerTweets(self):
        keywords = ['soccer', 'football','Crystal Palace','EPL', 'goal', 'SLeague', 'PREMIER LEAGUE'
                    'Norwich City', 'Southampton', 'Cardiff City', 'Stoke City', 'Newcastle United',
                    'Sunderland', 'Everton', 'West Bromwich Albion', 'Tottenham Hotspur',
                    'Liverpool', 'Chelsea', 'Manchester City', 'Man City', 'Everton', 'Arsenal', 'Tottenham', 'ManU', 'Manchester United', 'Southampton', 'Newcastle United', 'Newcastle ' ,'Stoke City', 'West Ham', 'Hull City', 'Swansea City', 'Fulham', 'Cardiff City', 'Sunderland']
        for word in keywords:
            resultSet = self.searchAPI(word, 150)
            self.writeToFile(resultSet, 'soccer', word)
        return True
    
    def searchBasketballTweets(self):
        keywords = ['NBA']
        for word in keywords:
            resultSet = self.searchAPI(word, 150)
            self.writeToFile(resultSet, 'basketball', word)
        return True    
    
    def searchF1Tweets(self):
        keywords = ['F1NightRace', 'SingaporeGP']
        for word in keywords:
            resultSet = self.searchAPI(word, 150)
            self.writeToFile(resultSet, 'F1', word)
        return True    
    
    def startBasicCrawling(self):
        #self.searchF1Tweets()
        #print "searching F1 Done.."
        self.searchSoccerTweets()
        print "searching soccer done.."
        #self.searchBasketballTweets()
        #print "searching basketball Done.."
        return
    
c = FixedKeywordCrawler()
c.startBasicCrawling()
    
    
    
    
    
    
    