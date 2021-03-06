import sys
from shutil import which
import selenium
from selenium import webdriver
import traceback
import sys
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ChromeBrowser(object):
    def __init__(self, setting):
        super().__init__()
        self.setting = setting
        self.options = Chrome_Options()
        profile_path = r"user-data-dir={}".format(setting["CHROME_PROFILE_PATH"])
        profile = r"profile-directory={}".format(setting["CHROME_PROFILE"])

        if setting["CHROME_PROFILE"].lower() != "null":
            self.options.add_argument(profile_path)
            self.options.add_argument(profile)
            #self.options.add_argument(f"user-data-dir={setting['CHROME_PROFILE']}")
        if setting["HEADLESS"].lower() == "true":
            self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--window-size=1920x1080")
        self.options.add_argument("--start-maximized")
        # chrome doesn't have proxy option
        self.options.add_experimental_option("detach", True)
        ''' codeBlock: disable automatic control to bypass cloudflare by remove navigator.webdriver flag 
        google chrome only'''
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        ''' changing user agent - this is not really needed but in case selenium use unmatch user agent associate with the version of chrome.'''
        if setting["USER_AGENT"] is not None:  # find user agent from search engine
            #self.options.add_argument(self.get_chrome_browser_agent())
            self.options.add_argument(setting["USER_AGENT"])


    def browser(self):
        browser = None
        try:
            browser = webdriver.Chrome(executable_path=self.setting["DRIVER_EXECUTABLE"], options=self.options)
        except:
            print("Might need to download new driver to match current installed version. download from https://chromedriver.chromium.org/downloads\nOR \n Close all the Google Chrome browser that currently open")
            #print(f"{traceback.format_exc()}")
            #sys.exit(1)
        return browser




