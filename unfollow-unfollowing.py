from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup webdriver
driver = webdriver.Firefox()
driver.get("https://twitter.com/login")

# log in
username = driver.find_element_by_css_selector("input[name='session[username_or_email]']")
password = driver.find_element_by_css_selector("input[name='session[password]']")
username.send_keys("YOUR_USERNAME")
password.send_keys("YOUR_PASSWORD")
driver.find_element_by_css_selector("button[type='submit']").click()

# go to profile page
driver.get("https://twitter.com/YOUR_PROFILE")

# get list of followers and following
followers = []
following = []

driver.get("https://twitter.com/YOUR_PROFILE/followers")
followers_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ol.UserList"))
)
for user in followers_list.find_elements_by_css_selector("li"):
    user_link = user.find_element_by_css_selector("a").get_attribute("href")
    followers.append(user_link)

driver.get("https://twitter.com/YOUR_PROFILE/following")
following_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "ol.UserList"))
)
for user in following_list.find_elements_by_css_selector("li"):
    user_link = user.find_element_by_css_selector("a").get_attribute("href")
    following.append(user_link)

# unfollow users who don't follow back
for user in following:
    if user not in followers:
        driver.get(user)
        driver.find_element_by_css_selector("button.follow-text").click()
        unfollow_confirm = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.unfollow-text"))
        )
        unfollow_confirm.click()

# close the driver
driver.quit()
