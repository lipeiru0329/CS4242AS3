import os
import twitter

from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

def login():

    # Go to http://twitter.com/apps/new to create an app and get these items
    # See also http://dev.twitter.com/pages/oauth_single_token

    APP_NAME = ''
    CONSUMER_KEY = '2JRLM23QHyLyBABuqg4tqQ'
    CONSUMER_SECRET = 'avpoP356DDKbHtTRiicjKBC01yXqfaI8QCgfZebmjA'
    TOKEN_FILE = 'auth/twitter.oauth'

    '''
        consumer_key = '2JRLM23QHyLyBABuqg4tqQ'
        consumer_secret = 'avpoP356DDKbHtTRiicjKBC01yXqfaI8QCgfZebmjA'
        access_token = '20692466-4kkQfaO8V0e2cVBDzfYg4EkFdQO9u0CNZLoP8Xma5'
        access_token_secret = '0bUGan28R0Dt2f0NIIjA2AcCkNUelANx674aWUH9Oj08f'
    '''
    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
    except IOError, e:
        (oauth_token, oauth_token_secret) = oauth_dance(APP_NAME, CONSUMER_KEY,
                CONSUMER_SECRET)

        if not os.path.isdir('auth'):
            os.mkdir('auth')

        write_token_file(TOKEN_FILE, oauth_token, oauth_token_secret)

    return twitter.Twitter(domain='api.twitter.com', api_version='1.1',
                        auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                        CONSUMER_KEY, CONSUMER_SECRET))
    
login()