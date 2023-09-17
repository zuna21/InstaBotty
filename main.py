from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from xpath import *
import json

def read_config():
    try:
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
        return config_data
    except FileNotFoundError:
        print("Error: config.json file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Unable to parse config.json. Make sure it's valid JSON.")
        return None

config = read_config()
if config == None:
    print("An Error accured.")
else:
    browser = webdriver.Firefox()

    browser.get("https://www.instagram.com")
    time.sleep(10)


    browser.find_element(By.XPATH, Xpath.username_xpath).send_keys(config["username"])
    browser.find_element(By.XPATH, Xpath.password_xpath).send_keys(config["password"])
    browser.find_element(By.XPATH, Xpath.login_button_xpath).click()
    time.sleep(10)

    browser.find_element(By.XPATH, Xpath.search_svg_xpath).click()
    time.sleep(5)

    browser.find_element(By.XPATH, Xpath.search_input_xpath).send_keys(config["target"])
    time.sleep(5)

    browser.find_element(By.XPATH, Xpath.betprediction_xpath).click()
    time.sleep(10)

    browser.find_element(By.XPATH, Xpath.followers_xpath).click()
    time.sleep(5)

    for _ in range(15):
        buttons = browser.find_elements(By.XPATH, "//button")
        for btn in buttons:
            if btn.text == "Follow":
                btn.click()
                time.sleep(3)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)



    time.sleep(5)
    browser.close()


