import Utils
import Counter

class ExpertIndexer():
    def __init__(self):
        self.userList = None
        self.u = Utils.Utils()
        self.topicDictionary = {}
        
    # Third, we want the freq occuring topics from the List Meta data [userid, list-id, name-meta , description-meta]
        #meta[0]: userid
        #meta[1]: list id
        #meta[2]: title
        #meta[3]: description
    def TopicWordProcessor(self, fileListMeta):
        f = open(fileListMeta)
        for meta in f:
            titleList = u.CamelCaseProcessor(meta[2]) # process camelcasetitle first
            combinedTitleAndDesc = titleList.extend(meta[3].split()) # combine title and description
            languageProcessedList = u.CommonLanaguageProcessor(combinedTitleAndDesc)
            POSProcessedList = u.POSNounADJProcessor(langauageProcessedList)
            RemovedCloseWordsList = u.EditDistanceWordsRemover(POSProcessedList)
            # dic format = userid->processed title + desc
            if self.topicDictionary.has_key(meta[0]):
                self.topicDictionary[meta[0]].extend(RemovedCloseWordsList)
            else:
                self.topicDictionary[meta[0]] = RemovedCloseWordsList
        for keys in self.topicDictionary:
            self.topicDictionary[keys] = collections.Counter(self.topicDictionary[keys])
        #f = open("dict.txt",'w')
        #json.dump(self.topicDictionary,f)
        #f.close()
        return
    
    def TopicWordIndexer(self):
        
        return
    
def main():
    t = ExpertIndexer()
    return True

main()
