import Utils
from twitter import *
import twitter__login
import json

twitter = Twitter()
class UserListCrawler():
    def __init__(self):
        self.listOfFiles = None
        self.listOfUsers = []
        self.listOfUserList = [] #(id, title, des)
        self.twitter_rest = twitter__login.login()
        self.listOfListsMetaInfo = {}
        pass
    
    def CrawlUserList(self,aspect):
        u = Utils.Utils()
        # First, we get the list of users
        self.listOfFiles = u.GetAllFilename("./data/"+aspect)
        for fn in self.listOfFiles:
            uf = open(fn,'r')
            for ufn in uf:
                self.listOfUsers.append(ufn.strip())
        
        # Second, we start crawl the user's twitter List meta data
        for user in self.listOfUsers:
            # this will return the list the user ownself created and add ppl in
            resultSet = self.twitter_rest.lists.ownerships(user_id = user)
            # this will return the list other ppl creates but user subscribes to it
            resultSet2 = self.twitter_rest.lists.subscriptions(user_id = user)
            # this will return the list that other people create and has the user inside 
            resultSet3 = self.twitter_rest.lists.memberships(user_id = user)
            # dictionary[userid]-> (list-id,name-meta, description-meta)
            for r in resultSet["lists"]:
                self.listOfListsMetaInfo[user] = (r["id"],r["name"],r["description"])
        return

        # Third, we want the freq occuring topics from the List Meta data
        # Fourth, we want evaluate quality of expertise inference
        
        # Last, we need to store all inference into MongoDB
        # Build a search system to compare query and topic vector to return user result
        # Run Celery to update the topics -- extra

'''
    def getOwnList(self):
        # this will return the list the user ownself created and add ppl in
        resultSet = self.twitter_rest.lists.ownerships(screen_name = 'socialmediaanal')
        # this will return the list other ppl creates but user subscribes to it
        resultSet2 = self.twitter_rest.lists.subscriptions(screen_name = 'socialmediaanal')
        # this will return the list that other people create and has the user inside 
        resultSet3 = self.twitter_rest.lists.memberships(screen_name = 'socialmediaanal')
        try:
            print resultSet["lists"][0]["name"]
            print resultSet["lists"][0]["description"]
            print resultSet2["lists"][0]["name"]
            print resultSet2["lists"][0]["description"]
            print resultSet3["lists"][0]["name"]
            print resultSet3["lists"][0]["description"]
        except:
            pass
        return
'''

def main():
    uc = UserListCrawler()
    #uc.CrawlUserList()
    #uc.getUserList()
    uc.getOwnList()
    return True

main()
