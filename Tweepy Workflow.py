# Introduction to Twitter Scraping with Tweepy

# use this script to experiment!

# Note: 
### these lines are ToDos!  

#%% --- Motivation (optionally):
# here we should show how hard it is to get data from Twitter w/o Tweepy
# ...and that Twitter doesn't like to be scraped manually...
# see https://twitter.com/robots.txt for scraping etiquette... be polite!


#%% --- Setting Up:
# first we need to import tweepy
# install by typing the following to your terminal: 
# pip install tweepy 
import tweepy

# Next we have to authenticate
# ...there are two ways:

#%% --- application-user (OAuth1a):
auth = tweepy.OAuthHandler(api_key, api_secret_key, callback_url)
# you get the first two at https://dev.twitter.com/apps/new (You need a Twitter Account!)
# Set up Callback URL when you configure your profile on twitter.com (if it doesn't change)

# now we need a request token:
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

### don't really understand this yet!
session.set('request_token', auth.request_token['oauth_token'])
# Example using callback (web app)
verifier = request.GET.get('oauth_verifier')
# Example w/o callback (desktop)
verifier = raw_input('Verifier:')

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



#%% Get Tweets:
# print all public posts in your own timeline: 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)



#%% --- User data
# Let's get some info about a user:
# Get the User object for twitter...
user = api.get_user(screen_name='realDonaldTrump')
### would be a great example, but does it work for banned accounts?

# Username:
print(user.screen_name)

# Number of followers:
print(user.followers_count)

# A list of followers:
for friend in user.friends():
   print(friend.screen_name)