## **Capstone Project**

This is the Capstone Project for the CodingNomads Python Course.

In this project I had to collect data from a bunch of tweets using Tweepy python Library, in order to get:

- The average number of followers.
- The average length of tweets (counting words).
- The average length of tweets (counting characters).
- The percentage of tweets that have a hashtag (#).
- The percentage of tweets that have a mention (@).
- The 100 most common words.
- The 100 most common symbols.
- Percentage of tweets that use punctuation.
- The longest word in a tweet.
- Shortest word in a tweet.
- What user has the most tweets in the dataset.
- The average number of tweets from an individual user.
- The hour with the greatest number of tweets.

**How to make it work?**
--------------------

First of all, you need to create a Twitter account and get your own credentials to connect to the Twitter API.

Once you have them, you can create the connection to the database using the *Tweepy* module.
In my case I was extracting data for tweets related to **NBA** topic.

Once I got all the information using the functions I created, I posted all data to MySQL Database (used MySQL Workbench) on 2 different tables.


**Libraries/Modules I used**
----------------------------

![image](../12_packages_modules/CodingNomads_files/image.png)

