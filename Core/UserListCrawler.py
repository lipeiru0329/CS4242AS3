import Utils
from twitter import *
import twitter__login
import json

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
        pass
    
    def GetAllUsersFromTwitterCrawl(self, aspect):
        u = Utils.Utils()
        # First, we get the list of users that has been crawled recently
        self.listOfFiles = u.GetAllFilename("./data/"+aspect+"/user/")
        for fn in self.listOfFiles:
            uf = open(fn,'r')
            for ufn in uf:
                self.listOfUsers.append(ufn.strip())
            uf.close()
        self.listOfUsers = list(set(self.listOfUsers))
        return self.listOfUsers
    
    # Second, we start crawl the user's twitter List meta data
    # We want to know if the user who tweeted is an expert? so take her Member column
    def CrawlUserListMeta(self):
        for user in self.listOfUsers:
            # a) These 2 appear in twitter as user's List Subscribed to
            #resultSet = self.twitter_rest.lists.ownerships(user_id = user) # this will return the list the user OWNSELF created ONLY and add ppl in
            #resultSet = self.twitter_rest.lists.subscriptions(user_id = user) # this will return the list other ppl creates but user subscribes to it
            
            # b) This appear in twitter List Member of
            resultSet = self.twitter_rest.lists.memberships(user_id = user) # This will return the list that other people create and has the user inside 
            
            # format of list is [userid, list-id, name-meta , description-meta]
            # We will try the list the user has created and added ppl in
            if len(resultSet["lists"])>0:
                for r in resultSet["lists"]:
                    self.listOfListsMetaInfo.append((user, r["id"], r["name"], r["description"]))
        '''
        f = open("./data/soccer/list/1.txt",'w')
        json.dump(self.listOfListsMetaInfo,f)
        f.close()
        '''
        return self.listOfListsMetaInfo

def main():
    uc = UserListCrawler()
    print uc.GetAllUsersFromTwitterCrawl("soccer")
    print uc.CrawlUserListMeta()
    return True

main()
