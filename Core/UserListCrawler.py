import Utils
from twitter import *
import twitter__login
import json, time, sys, os, shutil

twitter = Twitter()
'''
    THE INUITION: A user listed by many other users under a certain topic is likely to be expert
'''

class UserListCrawler():
    def __init__(self):
        self.listOfFiles = None
        self.listOfUsers = []
        self.listOfUserList = [] #(id, title, des)
        self.twitter_rest = twitter__login.login()
        self.listOfListsMetaInfo = []
        self.aspect = None
        self.u = Utils.Utils()
        pass
    '''
        Here we want to chucnk all recent userids into 15users per file for api limit
    '''
    def ChunkAllUsersFromTwitterCrawl(self, aspect):
        self.aspect = aspect
        # First, we get the list of users that has been crawled recently
        self.listOfFiles = self.u.GetAllFilename("./data/"+aspect+"/users/")
        for fn in self.listOfFiles:
            uf = open(fn,'r')
            for ufn in uf:
                self.listOfUsers.append(ufn.strip())
            uf.close()
            os.remove(fn) # remove file after done
        self.listOfUsers = list(set(self.listOfUsers))
        i = 1
        tempChuckList = []
        while len(self.listOfUsers) > 0:
            tempChuckList.append(self.listOfUsers.pop())
            if len(tempChuckList) == 15:
                luf = open("./data/"+aspect+"/listOfUsers"+"-"+str(i)+"-"+time.strftime('%Y%m%d-%H%M%S')+".txt",'w')
                json.dump(tempChuckList,luf)
                luf.close()
                tempChuckList = []
                i+=1
        if len(tempChuckList) > 0:
            luf = open("./data/"+aspect+"/listOfUsers"+"-"+str(i)+"-"+time.strftime('%Y%m%d-%H%M%S')+".txt",'w')
            json.dump(tempChuckList,luf)
            luf.close()
        return
    
    # Second, we start crawl the user's twitter List meta data
    # We want to know if the user who tweeted is an expert? so take her Member column!
    # can only be done for 1 file. Need to optimise for queqing up
    def CrawlUserListMeta(self):
        self.listOfFiles = self.u.GetAllFilename("./data/"+self.aspect+"/")
        firstFile = self.listOfFiles[0]
        with open(firstFile) as f:
            data = f.read()
            self.listOfUsers = json.loads(data)
        for user in self.listOfUsers:
            # b) This appear in twitter List Member of
            resultSet = {}
            try:
                resultSet = self.twitter_rest.lists.memberships(user_id = user) # This will return the list that other people create and has the user inside 
            # format of list is [userid, list-id, name-meta , description-meta]
            # if user is a member of > 3 PUBLIC list
                if len(resultSet["lists"])>3:
                    for r in resultSet["lists"]:
                        self.listOfListsMetaInfo.append((user, r["id"], r["name"], r["description"]))
            except Exception as inst:
                print "Rate Limit Exceeded. Break it out!"
                break # need to change this break since it will miss out some users!!
        #housekeeping, we move the done file out
        destOfDoneList = "./data/"+self.aspect+"/donelist/"
        shutil.move(firstFile,destOfDoneList)
        return self.listOfListsMetaInfo
    
    def SaveUserListMetaInfo(self):
        fname = "./dict/"+self.aspect+"/UserListMetaInfo/"+time.strftime('%Y%m%d-%H%M%S')+".txt"
        f = open (fname, 'w')
        json.dump(self.listOfListsMetaInfo,f)
        f.close()
        return

'''
We need to schedule this to run every 15+mins using django celery
'''

def main():
    uc = UserListCrawler()
    uc.ChunkAllUsersFromTwitterCrawl("soccer")
    uc.CrawlUserListMeta()
    uc.SaveUserListMetaInfo()
    return True

main()
