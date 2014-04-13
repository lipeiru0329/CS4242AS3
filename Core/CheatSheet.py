import os
import json

'''
#Joins a list into string
'''
my_list = ["Hello", "world"]
print " ".join(my_list)

'''
#parse JSON string and returns it as a Python data
'''
def JSONDecoder(fileName):
    tweets = []
    for line in open(fileName):
        try: 
          tweets.extend(json.loads(line)) 
        except:
          pass
    return tweets

'''
encoding decoding
loads("stringhere")
load(filestream)
dumps  : you want to write to a file or network stream
'''
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
data_string = json.dumps(data)
print 'ENCODED:', data_string #ENCODED: [{"a": "A", "c": 3.0, "b": [2, 4]}]
decoded = json.loads(data_string)
print 'DECODED:', decoded  #DECODED: [{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]
print 'ORIGINAL:', type(data[0]['b']) #ORIGINAL: <type 'tuple'>
print 'DECODED :', type(decoded[0]['b']) #DECODED : <type 'list'>



'''
Remove Duplicates
'''
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print t #[1, 2, 3, 1, 2, 5, 6, 7, 8]
print list(set(t)) #[1, 2, 3, 5, 6, 7, 8]
s = [1, 2, 3]
print list(set(t) - set(s)) #[8, 5, 6, 7]


