import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time

load_dotenv()

class CityTextBoxTest(unittest.TestCase):
    def setUp(self):
      options = Options()
      options.binary_location =  os.getenv('CHROME_BIN')
      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def tearDown(self):
      self.driver.quit()

    def test_search_field(self):  # add 'self' as the first parameter
      self.driver.get('http://localhost:3000')
      WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.NAME, 'city')))

      # Find the search field element by its name attribute
      search_field = self.driver.find_element(By.NAME, 'city')

      # Input 'Istanbul' into the search field
      search_field.send_keys('Istanbul')
      search_field.send_keys(Keys.RETURN)  # simulate the ENTER key

      # Allow the page to load results for a while
      time.sleep(2)

      # Check if the city name is correctly updated
      city_name = self.driver.find_element(By.ID, 'country').text 
      assert city_name.startswith('Istanbul'), f'Expected city name to start with "Istanbul", but got {city_name}'

if __name__ == '__main__':
    unittest.main()
