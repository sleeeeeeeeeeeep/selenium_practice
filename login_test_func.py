# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver():
    # setup
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver

    # teardown
    driver.quit()

def test_incorrectpassword(driver):
    driver.set_window_size(1297, 609)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauc")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
    assert len(elements) > 0
    assert driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"

def test_incorrectusername(driver):
    driver.set_window_size(1270, 822)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_use")
    driver.find_element(By.CSS_SELECTOR, ".login_wrapper-inner").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
    assert len(elements) > 0
    assert driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"

def test_loginlockedoutuser(driver):
    driver.set_window_size(1270, 822)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("locked_out_user")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
    assert len(elements) > 0
    assert driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Sorry, this user has been locked out."

def test_loginstandarduser(driver):
    driver.set_window_size(1270, 822)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.ID, "header_container")
    assert len(elements) > 0
    elements = driver.find_elements(By.ID, "inventory_container")
    assert len(elements) > 0

def test_noinputpassword(driver):
    driver.set_window_size(1270, 822)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
    assert len(elements) > 0
    assert driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Password is required"

def test_noinputusername(driver):
    driver.set_window_size(1270, 822)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
    assert len(elements) > 0
    assert driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"

def test_noinputusernamepassword(driver):
    driver.set_window_size(1270, 822)
    driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
    assert len(elements) > 0
    assert driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"
