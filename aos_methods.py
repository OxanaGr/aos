from selenium import webdriver
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
import sys

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)
print('_____________________________________________________________________________________________________')


def SetUp():
    print(f' Advantage Shopping homepage')
    print('_____________________________________________________________________________________________________')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(' https://advantageonlineshopping.com/')
    if driver.current_url == locators.Main_Page:
        print('Advantage Shopping website Launched Successfully')
        print(f'Advantage Shopping URL: {driver.current_url}\nHome Page Title: {driver.title}')
        print(f'__________________Test started successfully at {datetime.datetime.now()}__________________')
        sleep(0.25)
    else:
        print(f'Advantage Shopping website didn\'t launch. Pleas check your code and try again!')
        print(f'Current URL is: {driver.current_url}, The Page Title is: {driver.title}')
    sleep(0.25)
    print('_____________________________________________________________________________________________________')


def CrtNwAcnt():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(5)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "usernameRegisterPage")]').send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "emailRegisterPage")]').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "passwordRegisterPage")]').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "confirm_passwordRegisterPage")]').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "first_nameRegisterPage")]').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "last_nameRegisterPage")]').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "phone_numberRegisterPage")]').send_keys(locators.phone_number)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "cityRegisterPage")]').send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "addressRegisterPage")]').send_keys(locators.address)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "state_/_province_/_regionRegisterPage")]').send_keys("BC")
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[contains(@name, "postal_codeRegisterPage")]').send_keys(locators.postal_code)

    driver.find_element(By.XPATH, '//input[contains(@name, "i_agree")]').click()
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, 'button#register_btnundefined').click()
    sleep(0.3)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.username}")]').is_displayed()
    sleep(0.3)
    print(F'New Account created\nUsername is: {locators.username}')


def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(0.3)
    print('_____________________________________________________________________________________________________')


def Login():
    driver.find_element(By.XPATH, '//*[@id="menuUserSVGPath"]').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//input[contains(@name, "username")]').send_keys(locators.username)
    driver.find_element(By.XPATH, '//input[contains(@name, "password")]').send_keys(locators.password)
    sleep(0.3)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.3)
    assert driver.find_element(By.XPATH, f'//*[contains(.,"{locators.username}")]').is_displayed()
    sleep(0.3)
    print(f'__________________!LogIn to {locators.username} account Successfully!__________________')
    print(f'__________________________Testedmat {datetime.datetime.now()}__________________________')


def TearDown():
    if driver is not None:
        print(f'__________________Test finished successfully at {datetime.datetime.now()}__________________')
        sleep(2)
        driver.close()
        driver.quit()

        logger('delleted')


def logger(action: object) -> object:
    old_instance = sys.stdout
    log_file = open('message.log', 'a')
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.username}\t'
          f'{locators.password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


SetUp()
CrtNwAcnt()
log_out()
Login()
TearDown()