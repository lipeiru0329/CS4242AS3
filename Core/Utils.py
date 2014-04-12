import nltk
import json
import re
from pprint import pprint
from os import walk

class Utils():

    def __init__(self):
        self.porterStemmer = nltk.PorterStemmer()
        self.stopwordsList = nltk.corpus.stopwords.words("english")
        self.wordNetLemmatizer = nltk.WordNetLemmatizer()
        
    def JSONDecoder(self,fileName):
        tweets = []
        for line in open(fileName):
            try: 
              tweets.extend(json.loads(line)) #parse JSON string and returns it as a Python data
            except:
              pass
        return tweets
    
    def GetAllFilename(self,fileDirectory):
        ListOfJSONFileName = []
        for (dirpath, dirnames, filenames) in walk(fileDirectory):
            for f in filenames:
                ListOfJSONFileName.append("".join(("".join(dirpath) + "" + "".join(f))))
            break
        return ListOfJSONFileName
    
#u = Utils()
#u.JSONDecoder("singapore-20140410-191221.json")
#u.GetJSONFileName("../data/all-stream/")