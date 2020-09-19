from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

Account_Username = input("Enter your Instagram account's Username:")
Account_Password = input("Enter your Instagram account's Password:")
website = webdriver.Firefox(executable_path="geckodriver-v0.27.0-linux64/geckodriver")
running = True


class instagram:
    def __init__(self, account_username, account_password, driver):
        self.account_username = account_username
        self.account_password = account_password
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        username = self.driver.find_element_by_css_selector("[name='username']")
        username.send_keys(Account_Username)
        password = self.driver.find_element_by_css_selector("[name='password']")
        password.send_keys(Account_Password)
        submit = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit.click()
        time.sleep(5)
        SaveInfo = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        SaveInfo.click()
        time.sleep(5)
        PostNotification = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        PostNotification.click()
        time.sleep(4)

    def spam(self):
        direct = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
        direct.click()
        time.sleep(3)
        box1 = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div")
        box1.click()

        textbox = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        while True:
            textbox.send_keys("i love you")
            time.sleep(1)
            textbox.send_keys(Keys.ENTER)


run = instagram(Account_Username, Account_Password, website)
run.spam()
