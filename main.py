from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# opens a userprofile and gets the first 'n' tweets
def get_n_tweets(n, username):
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/{username}')

    wait = WebDriverWait(driver, 10)

    time.sleep(20)

    last_height = 10
    tweets = []
    while len(tweets) < n:
        driver.execute_script(f"window.scrollTo(0, {last_height+2});")
        time.sleep(0.1)
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

# opens explore page of twitter and gets the first 'n' tweets
def get_explore_tweets(n):
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/explore')

    time.sleep(20)

    last_height = 10
    tweets = []
    while len(tweets) < n:
        driver.execute_script(f"window.scrollTo(0, {last_height + 2});")
        time.sleep(0.1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        tweetDiv = driver.find_elements(By.XPATH, "//div[@dir='auto' and @lang='en']")[:n]
        for i, tweet in enumerate(tweetDiv):
            if len(tweet.text) > 1 and tweet.text not in tweets:
                tweets.append(tweet.text)
        last_height += 200
    print(tweets)
    print(len(tweets))
    input("Enter")

# given URL of a tweet, it will return the text in that tweet.
def get_tweet_from_URL(url):
    driver = webdriver.Chrome()
    driver.get(url)
    print("Sleeping")
    time.sleep(20)

    td = driver.find_element(By.XPATH, "//div[@data-testid='cellInnerDiv']")
    tweetDiv = td.find_elements(By.XPATH, "//div[@dir='auto' and @lang='en']")
    # tweetDiv = driver.find_elements(By.XPATH, "//div[@dir='auto' and @lang='en']")
    if (len(tweetDiv)>=1):
        tweet = tweetDiv[0].text
        print("Tweet:", tweet)
    input("Enter")


# get_n_tweets(10, 'elonmusk')
# get_explore_tweets(10)
get_tweet_from_URL("https://twitter.com/Exulansista/status/1654540589730521088")
