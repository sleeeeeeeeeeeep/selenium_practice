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

class TestLogin():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()
  
    def test_incorrectpassword(self):
        self.driver.set_window_size(1297, 609)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauc")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"

    def test_incorrectusername(self):
        self.driver.set_window_size(1270, 822)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_use")
        self.driver.find_element(By.CSS_SELECTOR, ".login_wrapper-inner").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username and password do not match any user in this service"
  
    def test_loginlockedoutuser(self):
        self.driver.set_window_size(1270, 822)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("locked_out_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Sorry, this user has been locked out."
  
    def test_loginstandarduser(self):
        self.driver.set_window_size(1270, 822)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.ID, "header_container")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "inventory_container")
        assert len(elements) > 0

    def test_noinputpassword(self):
        self.driver.set_window_size(1270, 822)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Password is required"
    
    def test_noinputusername(self):
        self.driver.set_window_size(1270, 822)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"

    def test_noinputusernamepassword(self):
        self.driver.set_window_size(1270, 822)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".error-message-container")
        assert len(elements) > 0
        assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Epic sadface: Username is required"
  