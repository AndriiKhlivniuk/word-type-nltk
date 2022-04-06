import collections
import nltk
import tweepy
from textblob import TextBlob
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from array import *
from collections import defaultdict
import time


def _calculate_languages_ratios(text):
    """
    Calculate probability of given text to be written in several languages and
    return a dictionary that looks like {'french': 2, 'spanish': 4, 'english': 0}
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Dictionary with languages and unique stopwords seen in analyzed text
    @rtype: dict
    """

    languages_ratios = {}

    '''
    nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    
    >>> wordpunct_tokenize("That's thirty minutes away. I'll be there in ten.")
    ['That', "'", 's', 'thirty', 'minutes', 'away', '.', 'I', "'", 'll', 'be', 'there', 'in', 'ten', '.']
    '''

    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]
   
    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements) # language "score"

    return languages_ratios


def detect_language(text):
    """
    Calculate probability of given text to be written in several languages and
    return the highest scored.
    
    It uses a stopwords based approach, counting how many unique stopwords
    are seen in analyzed text.
    
    @param text: Text whose language want to be detected
    @type text: str
    
    @return: Most scored language guessed
    @rtype: str
    """

    ratios = _calculate_languages_ratios(text)

    most_rated_language = max(ratios, key=ratios.get)

    return most_rated_language

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

def process_tweets(rutweet):

    print ("This is a tweet: ",rutweet,"\n")
    language = detect_language(rutweet)
    print ("Tweet language:",language, "\n")

    tok = nltk.word_tokenize(rutweet)
    tags = nltk.pos_tag(tok, lang='rus')



    dictionary = defaultdict(list)

    for k, v in tags:
        dictionary[v].append(k)


    for k, v in dictionary.items():
        print(k,v)

def catch_tweets(search_by):
    api_key='bJMwFlBEY9CoLlSM5VwQltlrL'
    api_secret_key='IM60JGzeAnQybog8VXx4tLAs1uYWmkAvjSOCQq5LoRm8O1T8AE'

    access_token='1048934245639569409-TbZXq29rIjYZl71FP7OgTjVNTixeUc'
    access_token_secret='xUJRpds5GB7cQlivw6GJONj6AiVx5PIbcwBJqzDTsLklf'	

    auth = tweepy.OAuthHandler(api_key,api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.search_tweets(search_by)
    counter = 1
    for tweet in public_tweets:
        print("----------------------TWEET NUMBER: ",counter,"-------------------------")
        rutweet= tweet.text
        process_tweets(rutweet)
        counter = counter+1

    



###########-------main--------##################

catch_tweets('дом')












