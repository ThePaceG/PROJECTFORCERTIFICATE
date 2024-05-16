import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pom.Pages.contact_us_page import Contact_Us

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    time.sleep(5)
    yield driver
    driver.quit()

def test_form(driver):
    contact_us_page = Contact_Us(driver)
    contact_us_page.open_page('https://mindrisers.com.np')
    time.sleep(5)


    name = "MindRiser"
    # email = 'class@mindrisers.com.np'
    email = 'class@@@@mindrisers.com.np'
    # phone = '9843217125'
    phone = '9888843217125'
    subject = "Quality assurance"
    message = "Hi, I am new here!"

    contact_us_page.enter_name(name)
    time.sleep(5)
    contact_us_page.enter_email(email)
    if contact_us_page.is_valid_email(email):
        contact_us_page.enter_email(email)
    else:
        print("Invalid email address")
    time.sleep(5)
    contact_us_page.enter_phone(phone)
    if contact_us_page.is_valid_phone(phone):
        contact_us_page.enter_phone(phone)
    else:
        print("Invalid phone number")
    time.sleep(5)
    contact_us_page.enter_subject(subject)
    time.sleep(5)
    contact_us_page.enter_message(message)
    time.sleep(10)
