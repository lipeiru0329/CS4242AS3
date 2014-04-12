import twitter
import WebApp.twitter__login
import csv

consumer_key = '2JRLM23QHyLyBABuqg4tqQ'
consumer_secret = 'avpoP356DDKbHtTRiicjKBC01yXqfaI8QCgfZebmjA'
access_token = '20692466-UHvKF9lGGyjhkyn1H5PX55nXdGbZsCmGOZo6Exaoy'
access_token_secret = 'FXEAFtjBvT9hRLxgPubBRUiv8sR7GTSpmVYoW9UArGLOi'   
 
'''
SEARCH API: https://dev.twitter.com/docs/api/1.1/get/search/tweets
'''

def searchAPI():
    t = WebApp.twitter__login.login()
    boston_res = t.search.tweets(q="patriots",geocode="42.350425,-71.026611,50mi",count=100)
    baltimore_res = t.search.tweets(q="patriots",geocode="39.291797,-76.59668,50mi",count=100)
    reslist = []
    tweetfields = set()
    
    for r in boston_res['statuses']:
        if len(reslist)<10:
            print len(reslist)
            r['searchloc'] = 'boston'
            reslist.append(r)
            tweetfields = tweetfields.union(r.keys())
        else:
            break
    
    for r in baltimore_res['statuses']:
        if len(reslist)<10:
            print len(reslist)
            r['searchloc'] = 'baltimore'        
            reslist.append(r)        
            tweetfields = tweetfields.union(r.keys())
        else:
            break
        
    fname = 'out/example_tweets.csv'
    f = open(fname,'w')
    #dw = csv.DictWriter(f,fieldnames=list(tweetfields))
    dw = csv.DictWriter(f,fieldnames=[u"text","searchloc"])
    dw.writeheader()
    
    for r in reslist:
        subd = {}
        for k in dw.fieldnames:
            if isinstance(r[k],unicode):
                subd[k] = r[k].encode('utf8')
            else:
                subd[k] = r[k]
        dw.writerow(subd)
    
    f.close()

'''
STREAM API: 
'''
def streamAPI():
    twitter_stream = twitter.TwitterStream(auth=twitter.oauth.OAuth(access_token, access_token_secret,consumer_key, consumer_secret))
    res = twitter_stream.statuses.filter(track='singapore')
    reslist = []
    tweetfields = set()
    for r in res:
        if len(reslist)<10:
            print len(reslist)
            reslist.append(r)
            tweetfields = tweetfields.union(r.keys())
        else:
            break
    print tweetfields
    print "==========="
    print reslist
    fname = 'out/example_tweets.csv'
    f = open(fname,'w')
    dw = csv.DictWriter(f,fieldnames=list(tweetfields))
    dw.writeheader()
    for r in reslist:
        dw.writerow({k:v.encode('utf8') if isinstance(v,unicode) else v for k,v in r.items()})    
    f.close()  
streamAPI()
