from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class GuviInsta:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(10)

    def quit(self):
        self.driver.quit()

    def getNumberOfFollowers(self):
        xpath = "(//button[@type='button'])[3]"
        return self.driver.find_element(by=By.XPATH, value=xpath).text

    def getNumberOfFollowing(self):
        xpath = "(//button[@type='button'])[4]"
        return self.driver.find_element(by=By.XPATH, value=xpath).text


url = 'https://www.instagram.com/guviofficial/'
obj = GuviInsta(url)
obj.boot()
print(obj.getNumberOfFollowers())
print(obj.getNumberOfFollowing())
obj.quit()