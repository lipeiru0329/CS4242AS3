import nltk
import json
import re
from os import walk
import collections

class Utils():

    def __init__(self):
        self.porterStemmer = nltk.PorterStemmer()
        self.stopwordsList = nltk.corpus.stopwords.words("english")
        self.wordNetLemmatizer = nltk.WordNetLemmatizer()
        self.domainSpecificList = ["twitter", "list"]
        self.listOfNounADJ = ["JJ", "JJR", "JJS", "NN", "NNS", "NNP"," NNPS"]
                              
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
        print listOfWords
        for word in listOfWords:
            if word[1] in self.listOfNounADJ:
                parsedWordList.append(word[0])
        if len(parsedWordList) < 1:
            return listOfWords
        return parsedWordList
    
    def CommonLanguageProcessor(self, listOfWords):
        cleanup = []
        for l in listOfWords:
            l = l.lower()
            if l not in self.stopwordsList and l not in self.domainSpecificList:
                if len(l)>3:
                    l = self.wordNetLemmatizer.lemmatize(self.porterStemmer.stem(l))
                if len(l)>2:
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

#u = Utils()
#u.JSONDecoder("singapore-20140410-191221.json")
#u.GetJSONFileName("../data/all-stream/")
#l = ["politica","politics","ORANGE", "grey","apple", "grey"]
#print u.CamelCaseProcessor(l)
#print u.POSNounADJProcessor(l)
#print u.EditDistanceWordsRemover(l)
#print u.WordsFrequencyCounter(l)