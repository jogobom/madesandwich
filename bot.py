# This version by Chris Preston but basically totally copied from Molly White's twitter bot tutorial
# https://github.com/molly/twitterbot_framework
# Thanks Molly.

import os
import tweepy
from secrets import *
from time import gmtime, strftime
import numpy as np

# ====== Individual bot configuration ==========================
bot_username = 'madesandwich'
logfile_name = bot_username + '.log'


# ==============================================================

def get_meat():
    return np.random.choice(
        ['Ham',
         'Beef',
         'Cumberland Sausage',
         'Bacon',
         'Brussels Pate',
         'Smoked Ham',
         'Italian Salami',
         'Chorizo',
         'Pastrami',
         'Smoked Turkey',
         'Chicken',
         'Chicken Tikka',
         'Parma Ham']
    )


def get_seafood():
    return np.random.choice(
        ['Tuna',
         'Tuna Mayo',
         'Creamy Crab',
         'Anchovies',
         'King prawns',
         'Small prawns',
         'Smoked Salmon']
    )


def get_dairy():
    return np.random.choice(
        ['Grated Cheese',
         'Cottage Cheese',
         'Cream Cheese',
         'Egg Mayo',
         'Sliced Egg',
         'Cheese Savoury',
         'Mature Cheddar',
         'Feta',
         'Brie',
         'Mozzarella',
         'Goats Cheese',
         'Emmental',
         'Apple Smoked Cheddar',
         'Stilton',
         'Parmesan']
    )


def get_veg():
    return np.random.choice(
        ['Red Onion',
         'Watercress',
         'Salad Cress',
         'Rocket',
         'Spinach',
         'Radish',
         'Sweetcorn',
         'Grated Carrot',
         'Beetroot',
         'Olives',
         'Grapes',
         'Apple',
         'Banana',
         'Pease Pudding',
         'Stuffing',
         'Raw Peppers',
         'Coleslaw',
         'Houmous',
         'Sun Blushed Tomato',
         'Avocado',
         'Roast Med Veg',
         'Roast Peppers',
         'Baked beans',
         'Pomegranate']
    )


def get_sauce():
    return np.random.choice(
        ['Ketchup',
         'English Mustard',
         'Wholegrain Mustard',
         'Dijon Mustard',
         'Vulture mustard',
         'Pickle',
         'Sweet Chilli',
         'Hot Chilli',
         'Hoi Sin',
         'Marie Rose',
         'Horseradish',
         'Caesar',
         'Cranberry Sauce',
         'Onion Marmalade',
         'Tomato Chutney',
         'Apple Chutney',
         'Mango Chutney',
         'Mint & Garlic Yoghurt',
         'BBQ Sauce',
         'Tomato Pesto',
         'Basil Pesto']
    )


def get_extras():
    return np.random.choice(
        ['Jalapenos',
         'Walnuts',
         'Pinenuts',
         'Watercress']
    )


def create_tweet():
    meat = np.random.choice([get_meat(), get_seafood()], p=[0.7, 0.3])
    veg = get_veg() + np.random.choice(['', ", {0}".format(get_veg())], p=[0.7, 0.3])
    dairy = np.random.choice([get_dairy(), ''], p=[0.7, 0.3])
    sauce = get_sauce()
    extras = np.random.choice([get_extras(), ''], p=[0.3, 0.7])
    text = 'SotD - ' + meat + ', '
    if dairy != '':
        text += dairy + ', '
    text += veg + ', ' + sauce
    if extras != '':
        text += ', ' + extras
    return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log('Tweeted: ' + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime('%d %b %Y %H:%M:%S', gmtime())
        f.write('\n' + t + ' ' + message)


if __name__ == '__main__':
    tweet_text = create_tweet()
    tweet(tweet_text)
