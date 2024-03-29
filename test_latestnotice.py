# Generated by Selenium IDE
import os
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLatestnotice():
  def setup_method(self, method):
    chrome_options = Options()
    prefs = {
      "download.default_directory": self.get_download_directory(),
      "download.prompt_for_download": False,
      "download.directory_upgrade": True,
      "plugins.always_open_pdf_externally": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    self.driver = webdriver.Chrome(options=chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def get_download_directory(self):
    # Specify default download directory relative to the script location
    default_directory = os.path.join(os.path.dirname(__file__), 'Downloads')
    # Check if the 'Downloads' directory exists, if not, create it
    if not os.path.exists(default_directory):
      os.makedirs(default_directory)
    return default_directory
  
  def test_latestnotice(self):
    # Go to the website
    self.driver.get("https://main.sci.gov.in/notices-circulars")
    # Wait for the link element to be visible and clickable
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(2) > a")))
    # Click on the link
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(2) > a").click()
    # Wait for the file to be downloaded
    time.sleep(3)

