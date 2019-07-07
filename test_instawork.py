from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class InstaWork(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(executable_path='.\Driver\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")
        time.sleep(3)

    def test_search_by_text(self):
        # identify the serach field and pass the key
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Instawork")
        self.search_field.submit()
        time.sleep(10)
        # identify the serach result and search for spefic url
        links = self.driver.find_elements_by_xpath("//div[@class='r']/a")
        for link in links:
            if 'www.instawork.com' in link.text:
                print(links.index(link)+1)
        time.sleep(3)

    def TearDown(self):
        self.dirver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
