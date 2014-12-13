from django.shortcuts import render
import twitter



consumer_key='hJvKiCJ2Px9anaSmzrWhk1hX4'
consumer_secret='0p1QGnahBjFNSt7oXRI9YprDJKWvxQ5DcOqvR4aQVVd5ceCCOg'
access_token_key='245798015-I6IinZBVwCluYEwc3zWCLpJ23FIl1C8DiB4h07Xu'
access_token_secret='66i5QMTU9wyNlc29xVOULYe4qpUb8MXZhJx85ZEAyYkae'



def get_tweets(screen_name="sondha_prodip",count=1):


    twitter_api=twitter.Api(consumer_key, consumer_secret, access_token_key,access_token_secret)
    #import pdb;pdb.set_trace()
    tweets = twitter_api.GetUserTimeline(screen_name, count)
    return tweets


def post_tweet(screen_name="sondha_prodip",update_text="here is the test"):
    twitter_api=twitter.Api(consumer_key, consumer_secret, access_token_key,access_token_secret)
    twitter_api.PostUpdate(update_text)


# Create your views here.
