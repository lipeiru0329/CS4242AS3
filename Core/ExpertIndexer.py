import Utils
import collections
import json
import os
import time

class ExpertIndexer():
    def __init__(self):
        self.userList = None
        self.u = Utils.Utils()
        self.topicDictionary = {}
        self.listOfFiles = None
        self.aspect = None
        self.listOfMeta = None
        
    # Third, we want the freq occuring topics from the List Meta data [userid, list-id, name-meta , description-meta]
        #meta[0]: userid
        #meta[1]: list id
        #meta[2]: title
        #meta[3]: description
    def TopicWordProcessor(self,aspect):
        self.aspect = aspect
        self.listOfFiles = self.u.GetAllFilename("./dict/"+self.aspect+"/UserListMetaInfo/")
        firstFile = self.listOfFiles[0] # need to change this!!
        with open(firstFile) as f:
            data = f.read()
            self.listOfMeta = json.loads(data)
        for meta in self.listOfMeta:
            titleList = []
            titleList.append(meta[2])
            titleList = self.u.CamelCaseProcessor(titleList) # process camelcasetitle first
            if len(meta[3].split()) >0:
                titleList.extend(meta[3].split()) # combine title and description
                combinedTitleAndDesc = titleList[:]
            else:
                combinedTitleAndDesc = titleList[:]
            normalizedProcessedList = self.u.normalizeText(combinedTitleAndDesc)
            languageProcessedList = self.u.CommonLanguageProcessor(normalizedProcessedList)
            POSProcessedList = self.u.POSNounADJProcessor(languageProcessedList)
            #RemovedCloseWordsList = self.u.EditDistanceWordsRemover(POSProcessedList)
            # dic format = userid->processed title + desc
            if self.topicDictionary.has_key(meta[0]):
                (self.topicDictionary[meta[0]]).extend(POSProcessedList) 
            else:
                self.topicDictionary[meta[0]] = POSProcessedList[:]        
        return
    
    '''
        We can make use of authoriative user algo to less the step to convert the dictionary and just write the topicdictionary
    '''
    def TopicWordIndexer(self):
        '''
            We need to converte topicDictionary to InvertedIndex
        '''
        invertedIndexDict = {}   
        for key in self.topicDictionary:
            c = collections.Counter(self.topicDictionary[key])
            for term in self.topicDictionary[key]:
                posting = [(key, c[term]),]
                #if invertedIndexDict[term]
                if invertedIndexDict.has_key(term):
                    (invertedIndexDict[term]).extend(posting) 
                else:
                    invertedIndexDict[term] = posting[:]
        '''
            lets start invertedindexing..unoptimised
        '''
        timef = str(time.strftime('%Y%m%d-%H%M%S'))
        indexFilename = "./dict/"+self.aspect+"/dict-"+timef+".txt"
        idxf = open(indexFilename,'w')    
        postingFilename = "./dict/"+self.aspect+"/postings-"+timef+".txt"
        idxp = open(postingFilename,'w')
        
        for key in invertedIndexDict:
            idxf.write(key.encode('utf-8')+"\n")
            l = []
            for i in invertedIndexDict[key]:
                l.append(str(i[0])+" "+ str(i[1]))
            idxp.write(" ".join(l)+"\n")
        idxf.close()
        idxp.close()
        return
    
def main():
    t = ExpertIndexer()
    t.TopicWordProcessor("soccer")
    t.TopicWordIndexer()
    return True

main()
