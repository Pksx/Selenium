import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service as Chromeservice
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
driver = webdriver.Chrome(service=Chromeservice(executable_path=chrome_driver_path))

driver.get('https://youtube.com')
sleep(5)