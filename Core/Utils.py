import nltk
import json
import re
from os import walk
import collections
import string
import unicodedata
import sys

TwitterDictionaryFile = './dict/emnlp_dict.txt'
class Utils():

    def __init__(self):
        self.porterStemmer = nltk.PorterStemmer()
        self.stopwordsList = nltk.corpus.stopwords.words("english")
        self.wordNetLemmatizer = nltk.WordNetLemmatizer()
        self.domainSpecificList = ["twitter", "list"]
        self.listOfNounADJ = ["JJ", "JJR", "JJS", "NN", "NNS", "NNP","NNPS" ,"IN"]
        self.emnlp = {} 
        self.prepareDictionary()
    '''
    Generate dictionary for use in informal language normalization
    '''
    def prepareDictionary(self):
        for line in open(TwitterDictionaryFile, 'r'):
            line = line.split()
            self.emnlp[line[0]] = line[1]
            
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
    
    def CamelCaseProcessor(self, listOfWords):
        parsedWordList = []
        for word in listOfWords:
            word = re.sub("([a-z])([A-Z])", "\g<1> \g<2>", word).split()
            parsedWordList.extend(word)
        return parsedWordList
    
    def POSNounADJProcessor(self, listOfWords):
        parsedWordList = []
        # tags from https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
        listOfWords = nltk.pos_tag(listOfWords)
        for word in listOfWords:
            if word[1] in self.listOfNounADJ:
                parsedWordList.append(word[0])
        if len(parsedWordList) < 1:
            return listOfWords
        return parsedWordList
    
    def CommonLanguageProcessor(self, listOfWords):
        cleanup = []
        t = " ".join(listOfWords)
        t = self.parseText(t)
        listOfWordsnew = t.split()
        for l in listOfWordsnew:
            l = l.lower()
            if len(l)>3:
                #l = self.porterStemmer.stem(l)
                l = self.wordNetLemmatizer.lemmatize(l)
                pass
            if len(l)>2 and l not in self.stopwordsList and l not in self.domainSpecificList:
                cleanup.append(l)
        return cleanup
    
    def EditDistanceWordsRemover(self,listOfWords):
        cleanup = []
        listOfWords = list(set(listOfWords))
        for word in listOfWords:
            if len(cleanup) == 0:
                cleanup.append(word)
            else:
                flag = False
                for cleanword in cleanup:
                    if nltk.metrics.edit_distance(word,cleanword) <= 2:
                        flag=True
                if flag == False:
                    cleanup.append(word)
                print cleanup
        return cleanup
    
    def normalizeText(self,listOfWord):
        cleanup = []
        for word in listOfWord:
            if self.emnlp.has_key(word):
                cleanup.append(self.emnlp[word].lower())
            else:
                cleanup.append(word.lower())
        return cleanup
    
    def parseText(self,tweetword):
        #Convert www.* or https?://* to URL
        text = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweetword)
        #remove @username
        text = re.sub('@[^\s]+','',text)
        #remove punctuation
        text = re.sub(ur"\p{P}+", "", text)
        #Remove additional white spaces
        text = " ".join(text.split())
        #Replace #word with word
        text = re.sub(r'#([^\s]+)', r'\1', text)
        #trim
        text = text.strip('\'"')
        return text

u = Utils()
#l = ["tmr","politicsNews","ORANGE", "grey","apple", "grey"]
#print u.normalizeText(l)
#u.JSONDecoder("singapore-20140410-191221.json")
#u.GetJSONFileName("../data/all-stream/")

#print u.CamelCaseProcessor(l)
#print u.POSNounADJProcessor(l)
#print u.EditDistanceWordsRemover(l)
#print u.WordsFrequencyCounter(l)