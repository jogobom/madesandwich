# This version by Chris Preston but basically totally copied from Molly White's twitter bot tutorial
# https://github.com/molly/twitterbot_framework
# Thanks Molly.

import os
import tweepy
from secrets import *
from time import gmtime, strftime
from random import choice
import numpy as np

# ====== Individual bot configuration ==========================
bot_username = 'madesandwich'
logfile_name = bot_username + '.log'


# ==============================================================

def get_meat():
    return choice(
        [('Ham', 50),
          ('Beef', 50),
         ('Cumberland Sausage', 50),
         ('Bacon', 50),
         ('Brussels Pate', 50),
         ('Smoked Ham', 60),
         ('Italian Salami', 60),
         ('Chorizo', 60),
         ('Pastrami', 70),
         ('Smoked Turkey', 70),
         ('Chicken', 70),
         ('Chicken Tikka', 70),
         ('Parma Ham', 90)]
    )


def get_seafood():
    return choice(
        [('Tuna', 70),
         ('Tuna Mayo', 70),
         ('Creamy Crab', 60),
         ('Anchovies', 60),
         ('King prawns', 100),
         ('Small prawns', 100),
         ('Smoked Salmon', 100)]
    )


def get_dairy():
    return choice(
        [('Grated Cheese', 50),
         ('Cottage Cheese', 50),
         ('Cream Cheese', 50),
         ('Egg Mayo', 60),
         ('Sliced Egg', 50),
         ('Cheese Savoury', 60),
         ('Mature Cheddar', 70),
         ('Feta', 60),
         ('Brie', 60),
         ('Mozzarella', 60),
         ('Goats Cheese', 70),
         ('Emmental', 70),
         ('Apple Smoked Cheddar', 70),
         ('Stilton', 70),
         ('Parmesan', 70)]
    )


def get_veg():
    return choice(
        [('Red Onion', 5),
         ('Watercress', 15),
         ('Salad Cress', 15),
         ('Rocket', 15),
         ('Spinach', 15),
         ('Radish', 15),
         ('Sweetcorn', 30),
         ('Grated Carrot', 30),
         ('Beetroot', 30),
         ('Olives', 40),
         ('Grapes', 30),
         ('Apple', 30),
         ('Banana', 30),
         ('Pease Pudding', 40),
         ('Stuffing', 50),
         ('Raw Peppers', 40),
         ('Coleslaw', 50),
         ('Houmous', 50),
         ('Sun Blushed Tomato', 50),
         ('Avocado', 50),
         ('Roast Med Veg', 50),
         ('Roast Peppers', 50),
         ('Baked beans', 50),
         ('Pomegranate', 50)]
    )


def get_sauce():
    return choice(
        [('Lemon Mayo', 15),
         ('Garlic Mayo', 15),
         ('Coronation Mayo', 25),
         ('Salad Cream', 15),
         ('Brown Sauce', 15),
         ('Ketchup', 15),
         ('English Mustard', 15),
         ('Wholegrain Mustard', 15),
         ('Dijon Mustard', 15),
         ('Vulture mustard', 20),
         ('Pickle', 20),
         ('Sweet Chilli', 20),
         ('Hot Chilli', 20),
         ('Hoi Sin', 20),
         ('Marie Rose', 20),
         ('Horseradish', 20),
         ('Caesar', 25),
         ('Cranberry Sauce', 25),
         ('Onion Marmalade', 25),
         ('Tomato Chutney', 25),
         ('Apple Chutney', 25),
         ('Mango Chutney', 35),
         ('Mint & Garlic Yoghurt', 25),
         ('BBQ Sauce', 25),
         ('Tomato Pesto', 35),
         ('Basil Pesto', 35)]
    )


def get_extras():
    return choice(
        [('Jalapenos', 30),
         ('Walnuts', 40),
         ('Pinenuts', 50)]
    )


def get_non_filling():
    return 'Houmous', 50


def create_tweet():
    tmp_array = [get_meat(), get_seafood(), get_non_filling(), ('', 0)]
    main_filling = tmp_array[np.random.choice(len(tmp_array), p=[0.53, 0.37, 0.06, 0.04])]

    veg1 = get_veg()

    tmp_array = [('', 0), get_veg()]
    veg2 = tmp_array[np.random.choice(len(tmp_array), p=[0.8, 0.2])]

    tmp_array = [get_dairy(), ('', 0)]
    dairy = tmp_array[np.random.choice(len(tmp_array), p=[0.7, 0.3])]

    sauce = get_sauce()

    tmp_array = [get_extras(), ('', 0)]
    extras = tmp_array[np.random.choice(len(tmp_array), p=[0.1, 0.9])]

    text = 'S.O.T.D '
    if main_filling[0] != '':
        text += main_filling[0] + ', '
    if dairy[0] != '':
        text += dairy[0] + ', '
    text += veg1[0] + ', '
    if veg2[0] != '':
        text += veg2[0] + ', '
    text += sauce[0]
    if extras[0] != '':
        text += ', ' + extras[0]

    price = 200 + main_filling[1] + veg1[1] + veg2[1] + dairy[1] + sauce[1] + extras[1]

    text += ', £{0:.2f}'.format(price / 100)

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
