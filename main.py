from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
# def get_last_n_tweets(username, n):
#     url = f"https://twitter.com/{username}"
#     driver = webdriver.Chrome()
#     driver.get(url)


# def get_last_n_tweets(username, n):
#     url = f"https://twitter.com/{username}"
#     driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver
#
#     driver.get(url)
#     time.sleep(2)
#
#     tweet_selector = "article div[data-testid='tweet']"
#     last_height = driver.execute_script("return document.body.scrollHeight")
#
#     tweets = []
#     print(f"last_height:{last_height} tweet_selector:{tweet_selector}")
#     while len(tweets) < n:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)
#         print("iter:")
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         # if new_height == last_height:
#         #     print("break")
#         #     break
#
#         last_height = new_height
#
#         tweets = driver.find_elements(By.CSS_SELECTOR, tweet_selector)[:n]
#         print(tweets)
#     for i, tweet in enumerate(tweets, start=1):
#         print(f"Tweet {i}: {tweet.text}")
#
#     # driver.quit()
#
#
# get_last_n_tweets("elonmusk", 5)  # Replace 'username_here' with the target user's username

# input("Enter")

def get_n_tweets(n, username):
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/{username}')

    # Define the expected condition and the maximum waiting time (e.g., 10 seconds)
    wait = WebDriverWait(driver, 10)

    # Wait for the presence of the main tweet container
    # wait.until(EC.presence_of_element_located((By.XPATH, "//div[@dir='auto' and @lang='en']")))
    print("sleeping")
    time.sleep(20)
    tweetDiv = driver.find_elements(By.XPATH, "//div[@dir='auto' and @lang='en']")[:10]
    for i, tweet in enumerate(tweetDiv):
        print("tweet:", tweet.text)


def get_n_hashtag_tweets(n, hashtag):
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/hashtag/{hashtag}')
    time.sleep(30)


def get_explore_tweets():
    driver = webdriver.Chrome()
    driver.get(f'https://twitter.com/explore')
    input("enter")


# get_n_tweets(10, 'elonmusk')
# get_n_hashtag_tweets(10, 'pti')

get_explore_tweets()

