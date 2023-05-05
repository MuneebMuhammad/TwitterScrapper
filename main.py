from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_n_tweets(n, username):
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/{username}')

    wait = WebDriverWait(driver, 10)

    time.sleep(20)

    last_height = 10
    tweets = []
    while len(tweets) < n:
        driver.execute_script(f"window.scrollTo(0, {last_height+2});")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        tweetDiv = driver.find_elements(By.XPATH, "//div[@dir='auto' and @lang='en']")[:n]
        for i, tweet in enumerate(tweetDiv):
            if len(tweet.text) >1 and tweet.text not in tweets:
                tweets.append(tweet.text)
        last_height += 200
    print(tweets)
    print(len(tweets))
    input("Enter")


def get_n_hashtag_tweets(n, hashtag):
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/hashtag/{hashtag}')
    time.sleep(30)


def get_explore_tweets():
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/explore')
    input("enter")


get_n_tweets(10, 'elonmusk')
# get_n_hashtag_tweets(10, 'pti')

# get_explore_tweets()

