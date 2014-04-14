import Utils
import collections
import linecache
import webbrowser

class ExpertQuerier():
    def __init__(self):
        self.u = Utils.Utils()
        self.termDictionary = {}

    # Build a search system to compare query and topic vector to return user result
    def prepareDictionary(self):
        idxf = open("./dict/soccer/dict-20140414-120801.txt")
        for term in idxf:
            l = term.split()
            self.termDictionary[l[0]] = (l[1],l[2])
        idxf.close()
        
    def TopicQueryProcessor(self,topicText):
        tf = 0
        idf = 0
        idpf = "./dict/soccer/postings-20140414-120801.txt"
        if self.termDictionary.has_key(topicText):
            n = self.termDictionary[topicText][1]
            uid = linecache.getline(idpf,int(n)).split()
            webbrowser.open('https://twitter.com/intent/user?user_id='+str(uid[0]))
        return
    
    # Last, we need to store all inference into MongoDB
    # Run Celery to update the topics -- extra
def main():
    t = ExpertQuerier()
    t.prepareDictionary()
    t.TopicQueryProcessor("soccer")
    return True

main()