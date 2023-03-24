from pathlib import Path
from time import sleep
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ROOT_FOLDER = Path (__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'

def make_chrome_browser (*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions ()

    if options is not None:
        for option in options:
            chrome_options.add_argument (option)

    chrome_service = Service (
        executable_path = str (CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service = chrome_service,
        options = chrome_options
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10

    
    options = ()
    browser = make_chrome_browser (*options)

    
    browser.get ("site")
    time.sleep (5)