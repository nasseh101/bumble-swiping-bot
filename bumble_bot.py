from selenium import webdriver
from time import sleep
from secrets import email, password

class BumbleBot():
  def __init__(self):
    self.driver = webdriver.Chrome()   

  def login(self):
    self.driver.get("https://bumble.com/")
    # Waiting for page to load
    sleep(3)

    signin_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
    signin_btn.click()
    sleep(3)

    fb_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div')
    fb_btn.click()

    base_window = self.driver.window_handles[0]
    self.driver.switch_to_window(self.driver.window_handles[1])

    email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
    email_in.send_keys(email)

    pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
    pw_in.send_keys(password)

    login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
    login_btn.click()
    self.driver.switch_to_window(base_window)

    # Delay to allow for Login
    sleep(4)

  def like(self):
    like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
    like_btn.click()

  def dislike(self):
    dislike_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]')
    dislike_btn.click()

  def handle_match_popup(self):
    cls_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div')
    cls_btn.click()

  def auto_swipe(self):
    while(True):
      sleep(1)
      try:
        self.like()
      except:
        self.handle_match_popup()


# bot = BumbleBot()
# bot.login() 
# bot.auto_swipe()