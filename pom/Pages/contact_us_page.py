from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import time
class Contact_Us:
    def __init__(self, driver):
        self.driver = driver
        self.name_textbox = (By.XPATH,"//input[@placeholder='Name']")
        self.email_textbox = (By.XPATH,"//input[@placeholder='Email']")
        self.phone_textbox = (By.XPATH,"//input[@placeholder='Phone']")
        self.subject_textbox = (By.ID, "subject")
        self.message_textbox = (By.ID, "message")
        self.submit_button = (By.XPATH, "//button[normalize-space()='Submit']")
    def open_page(self,url):
        self.driver.get(url)
        time.sleep(10)
        first_click = self.driver.find_element(*(By.XPATH,"//a[contains(text(),'contact us')]"))
        first_click.click()
        time.sleep(5)
        website_title = self.driver.title
        print(f"Website Title:{website_title}")
    def is_valid_email(self,email):
        email_pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
        return bool(re.match(email_pattern, email))
    def is_valid_phone(self, phone):
        phone_pattern = r"\d{10}$"
        return bool(re.match(phone_pattern, phone))
    def enter_name(self,name):
        # self.driver.find_element(*(By.XPATH,"//input[@placeholder='Name']")).send_keys(name)
         self.driver.find_element(*self.name_textbox).send_keys(name)
    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)
        #  self.driver.find_element(*(By.XPATH,"//input[@placeholder='Email']")).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)
        # self.driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']")).send_keys(phone)

    def enter_subject(self,subject):
        # self.driver.find_element(*self.message_textbox).send_keys(subject)
         self.driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']")).send_keys(subject)

    def enter_message(self,message):
        # self.driver.find_element(*self.message_textbox).send_keys(message)
         self.driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']")).send_keys(message)

    def click_submit(self):
        self.driver.find_element(*(By.XPATH,"//button[normalize-space()='Submit']")).click()