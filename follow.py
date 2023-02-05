from selenium import webdriver
import time

def follow_users_on_twitter(username, password, users_to_follow):
    # Initialize the web driver and log in to Twitter
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/login")
    time.sleep(2)

    username_input = driver.find_element_by_name("session[username_or_email]")
    username_input.send_keys(username)
    password_input = driver.find_element_by_name("session[password]")
    password_input.send_keys(password)
    password_input.submit()
    time.sleep(2)

    # Follow each user in the list
    for user in users_to_follow:
        # Navigate to the user's profile
        driver.get(f"https://twitter.com/{user}")
        time.sleep(2)

        # Check if the follow button is present and click it if it is
        try:
            follow_button = driver.find_element_by_xpath("//button[text()='Follow']")
            follow_button.click()
            time.sleep(2)
        except:
            pass
