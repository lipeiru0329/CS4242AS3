from django.shortcuts import render
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import tweetstream

def index(request):
    Tweets = getTweets()
    return render_to_response('index.html')


def getTweets():
    
    stream = tweetstream.SampleStream("howwk", "j4Wrr^39")
    Tweets = []
    for tweet in stream:
        Tweets.append(tweet)
    
    return True