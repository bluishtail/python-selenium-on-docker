import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class SampleGoogleTest(unittest.TestCase):
  def setUp(self):
    #ブラウザ起動
    self.driver = webdriver.Remote(
      command_executor=os.environ["SELENIUM_URL"],
      desired_capabilities=DesiredCapabilities.FIREFOX.copy()
    )
    #5秒停止
    time.sleep(5)
    #画面最大化
    self.driver.maximize_window()

  def tearDown(self):
    self.driver.quit()

  def test_check_google_translate_work_properly(self):
    self.driver.get("https://www.google.co.jp/")
    self.assertEqual(self.driver.current_url, "https://www.google.co.jp/")

if __name__ == '__main__':
  unittest.main(verbosity=2)
