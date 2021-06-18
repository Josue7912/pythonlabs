import os
import re
import tweepy
from pprint import pprint
import json
import collections
import sqlalchemy
import pymysql
import numpy as np
from time import gmtime, strftime
from collections import Counter
import datetime
from dateutil.parser import parse


## Authentication credentials come from txt file
with open('twittercredentials.txt', 'r') as f:
    text_creds = f.readlines()

# fetch the secrets from our virtual environment variables
CONSUMER_KEY = text_creds[0].strip()
CONSUMER_SECRET = text_creds[1].strip()
ACCESS_TOKEN = text_creds[3].strip()
ACCESS_SECRET = text_creds[4].strip()


# authenticate to the service we're accessing
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# create the connection
api = tweepy.API(auth)
tweets = [i for i in tweepy.Cursor(api.search,
               q="nba",
               lang="en",
               since=2017-1-1).items(100)]


# functions to execute tasks from capstone project
def avgnum_followers(tweets):
    total = 0
    all_users = 0
    for t in tweets:
        user = t.user.followers_count
        total += user
        all_users += 1
    return total / all_users

def avgtweetlength(tweets):
    lentweet = []
    for t in tweets:
        characcount = 0
        text = t.text.split()
        for word in text:
            characcount += 1
        lentweet.append(characcount)
    mean = np.mean(lentweet)
    return mean

def avg_character_len(tweets):
    lengtweet = []
    symbols = (".", ",", "/", "'", "!", "¡", "?", "¿", ")", "(", "[", "]", "+", "-", "*", ":", ";", "_")
    for t in tweets:
        charcount = 0
        text = t.text
        for word in text:
            for character in word:
                if character is not symbols:
                    charcount += 1
        lengtweet.append(charcount)
    mean = np.mean(lengtweet)
    return mean

def percent_tweet_punctuation(tweets):
    charcount = 0
    punctcount = 0
    symbols = (".", ",", "/", "'", "!", "¡", "?", "¿", ")", "(", "[", "]", "+", "-", "*", ":", ";", "_")
    lentweet = []
    for t in tweets:
        characcount = 0
        text = t.text
        for word in text:
            for char in word:
                charcount += 1
                characcount += 1
                if char in symbols:
                    punctcount += 1
        lentweet.append(characcount)
    mean = np.mean(lentweet)
    div = punctcount / charcount
    percentage = div * 100
    return percentage, mean

def percent_tweet_hashtag(tweets):
    hashtagcount = 0
    characcount = 0
    for t in tweets:
        text = t.text.split()
        for word in text:
            for char in word:
                characcount += 1
                if char == "#":
                    hashtagcount += 1
    div = hashtagcount / characcount
    percentage = div * 100
    return percentage

def percent_tweet_mention(tweets):
    mentioncount = 0
    characcount = 0
    for t in tweets:
        text = t.text.split()
        for word in text:
            for char in word:
                characcount += 1
                if char == "@":
                    mentioncount += 1
    div = mentioncount / characcount
    percentage = div * 100
    return percentage

def common_words(tweets):
    wordcount = {}
    print("Top 100 common words: ")
    for t in tweets:
        text = t.text.split()
        for word in text:
            word = word.replace(".", "").replace(",", "").replace(":", "").replace("\"", "").replace("!", "").replace("*", "").replace("-", "")
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(100):
        print(word, ": ", count)

def common_symbols(tweets):
    charactercount = {}
    print("Top 100 common symbols: ")
    for t in tweets:
        text = t.text
        for char in text:
            if char.isalpha() == False and char.isdigit() == False and char != " ":
                if char not in charactercount:
                    charactercount[char] = 1
                else:
                    charactercount[char] += 1
    character_counter = collections.Counter(charactercount)
    for char, count in character_counter.most_common(100):
        print(char, ": ", count)

def percent_tweet_punctuation(tweets):
    charcount = 0
    punctcount = 0
    symbols = (".", ",", "/", "'", "!", "¡", "?", "¿", ")", "(", "[", "]", "+", "-", "*", ":", ";", "_")
    for t in tweets:
        text = t.text
        for word in text:
            for char in word:
                charcount += 1
                if char in symbols:
                    punctcount += 1
    div = punctcount / charcount
    percentage = div * 100
    return percentage

def longestword(tweets):
    longest_word = ' '
    for t in tweets:
        text = t.text.split()
    return max(text,key=len)

def shortestword(tweets):
    for t in tweets:
        text = t.text.split()
    return min(text,key=len)

def usermost_tweets(tweets):
    usermost_tweets = 0
    username = " "
    for t in tweets:
        user = t.user.screen_name
        user_tweets = t.user.statuses_count
        if user_tweets > usermost_tweets:
            usermost_tweets = user_tweets
            username = user
    return(username, usermost_tweets)

def avgtweetxuser(tweets):
    tweet = 0
    all_tweets = 0
    for t in tweets:
        user_t = t.user.statuses_count
        tweet += user_t
        all_tweets += 1
    avg = tweet / all_tweets
    return avg

def greatesthour_tweet(tweets):
    hours = {}
    time = [t.user.created_at.strftime("%H") for t in tweets]
    for hour in time:
        if hour in hours:
            hours[hour] += 1
        else:
            hours[hour] = 1
    greatesthour = max(hours, key=hours.get)
    return greatesthour


print("The Average number of followers is: ", avgnum_followers(tweets))
print("The Average length of tweets (words) is: ", avgtweetlength(tweets))
print("The Average length of tweets (characters) is: ", avg_character_len(tweets))
print("The percentage of tweets that have a hashtag (#): ", percent_tweet_hashtag(tweets))
print("The percentage of tweets that have a mention (@): ", percent_tweet_mention(tweets))
common_words(tweets)
common_symbols(tweets)
print("The percentage of tweets that use punctuation: ", percent_tweet_punctuation(tweets))
print("The longest word in a tweet is :", longestword(tweets))
print("The shortest word in a tweet is : ", shortestword(tweets))
print("The user with most tweets is: ", usermost_tweets(tweets))
print("The average number of tweets from a user: ", avgtweetxuser(tweets))
print("The hour with major number of tweets is: ", greatesthour_tweet(tweets),"h")







## PUSH TO MYSQL DATABASE

engine = sqlalchemy.create_engine('mysql+pymysql://root:Vero7912.@localhost/twitter')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

twitter = sqlalchemy.Table('twitter', metadata,
sqlalchemy.Column('user_created', sqlalchemy.DateTime()),
sqlalchemy.Column('id', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('id_str', sqlalchemy.VARCHAR(50)),
sqlalchemy.Column('text', sqlalchemy.String(200)),
sqlalchemy.Column('expanded_url', sqlalchemy.String(100)),
sqlalchemy.Column('user_name', sqlalchemy.String(50)),
sqlalchemy.Column('followers_count', sqlalchemy.Integer()),
sqlalchemy.Column('statuses_count', sqlalchemy.Integer()))


twitter_results = sqlalchemy.Table('twitter results', metadata,
sqlalchemy.Column('avg_followers', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('tweet_length_word', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('tweet_length_char', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('percent_#', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('percent_@', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('100_common_words', sqlalchemy.JSON(300)),
sqlalchemy.Column('100_common_symbols', sqlalchemy.JSON(300)),
sqlalchemy.Column('percent_wit_punctuation', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('longest_words', sqlalchemy.JSON(200)),
sqlalchemy.Column('shortest_words', sqlalchemy.JSON(300)),
sqlalchemy.Column('user_most_tweets', sqlalchemy.JSON(50)),
sqlalchemy.Column('avg_num_tweets', sqlalchemy.VARCHAR(40)),
sqlalchemy.Column('greatest_hour_tweets', sqlalchemy.VARCHAR(40)))

metadata.create_all(engine)

tweet_list = [t._json for t in tweets]

for t in tweet_list:
    tweet_creation = parse(t['created_at'])
    create_at = tweet_creation.replace(tzinfo=None)
    twittervalues = {'user_created':create_at,
               'id': t['id'],
               'id_str': t['id_str'],
               'text':t['text'],
               'expanded_url':'https://twitter.com/twitter/statuses/'+str(t['id']),
                'user_name':t['user']['name'],
               'followers_count':t['user']['followers_count'],
               'statuses_count':t['user']['statuses_count']}

    query = sqlalchemy.insert(twitter).values(twittervalues)
    result_proxy = connection.execute(query)



tweetsresults = {'avg_num_tweets': avgtweetxuser(tweets),
                'tweet_length_char': avg_character_len(tweets),
                'tweet_length_word': avgtweetlength(tweets),
                'shortest_words':shortestword(tweets),
                'longest_words':longestword(tweets),
                'avg_followers':avgnum_followers(tweets),
                'percent_#':percent_tweet_hashtag(tweets),
                'percent_@':percent_tweet_mention(tweets),
                'percent_wit_punctuation':percent_tweet_punctuation(tweets),
                '100_common_words':common_words(tweets),
                '100_common_symbols':common_symbols(tweets),
                'user_most_tweets':usermost_tweets(tweets),
                'greatest_hour_tweets':greatesthour_tweet(tweets)}

query2 = sqlalchemy.insert(twitter_results).values(tweetsresults)
connection.execute(query2)


query3 = sqlalchemy.select(twitter_results)
result_proxy = connection.execute(query3)
result_set = result_proxy.fetchall()
pprint(result_set)