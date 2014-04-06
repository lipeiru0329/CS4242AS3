import tweepy
from tweepy import StreamListener
import json, time, sys
# Helper Class and methods
class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open('CS4242AppProject/data/F1/' + fprefix + '.' 
                            + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        self.delout  = open('CS4242AppProject/data/delete.txt', 'a')

    def on_data(self, data):
        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return False
        
    def on_status(self, status):
        self.output.write(status + "")
        self.counter += 1
        if self.counter >= 100:
            self.output.close()
            self.output = open('CS4242AppProject/data/F1/' + self.fprefix + '.' 
                               + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
            self.counter = 0
        return

    def on_delete(self, status_id, user_id):
        self.delout.write( str(status_id) + "")
        return

    def on_limit(self, track):
        sys.stderr.write(track + "")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...")
        time.sleep(60)
        return  