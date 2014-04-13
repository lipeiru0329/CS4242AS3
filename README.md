CS4242AS3
=========

SocialMediaComputingApp: Topic Expert Finder (Soccer optimised)
------------------------

App : Holds the python files for the Website

Core : Holds the python files for the processing, crawlers, authority user indentification, testing should fall here.
-- auth: holds the twitter authentication files
-- data: holds the crawled data splitted into aspects
-- dict: holds the invertedIndex dict&postings(generated), and twitterdictonary
-- testers & TestScripts: holds the tester files
-- ExpertIndexer.py : To index the experts (Done, unoptimised for processing)
-- ExpertQuerier.py: To query the invertedIndex (UNDONE)
-- FixedKeywordCrawler.py: uses Search API
-- StreamCrawler.py: uses StreamAPI
-- twitter_login.py: for twitter auth
-- UserListCrawler.py: uses REST API to crawl userlist (unoptimised, need to cron every 15 mins)
-- Utils.py: misc. functions for other classes (unoptimised)

Db : Holds the MongoDB files, please modify the mongo.config file

Documents : Holds the documentation, papers to follow

Include, Lib, Scripts : Files for the application virtualenv, please do not edit.

Static : Website GUI files

-----------------------------------------------------------------------------------------------------------------------

*Note:
Please do the normal python programming in Core folder, it will be integrated into the WebGUI once each function is done.
