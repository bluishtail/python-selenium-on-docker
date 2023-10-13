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
    url = "https://www.google.co.jp/"
    self.driver.get(url)
    self.assertEqual(self.driver.current_url, url)

if __name__ == '__main__':
  unittest.main(verbosity=2)

# クラス名: 任意。unittest.TestCaseを継承する
# メソッド名:
#   - test_から始まるメソッドが自動で実行される。テスト内容を書く
#   - setUp: 各テストメソッドの前に自動で実行される
#   - tearDown: 各テストメソッドの後に自動で実行される
