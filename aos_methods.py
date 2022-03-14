from selenium import webdriver
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import sys

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)
print('__________________________________________________________________________________________')


def SetUp():
    print(f' Advantage Shopping homepage')
    print('__________________________________________________________________________________________')
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
    print('__________________________________________________________________________________________')


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
    print(f'New Account created\nUsername is: {locators.username}')


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.6)
    print(f'Log out at {datetime.datetime.now()}')
    print('__________________________________________________________________________________________')


def Login():
    driver.find_element(By.XPATH, '//*[@id="menuUserSVGPath"]').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//input[contains(@name, "username")]').send_keys(locators.username)
    driver.find_element(By.XPATH, '//input[contains(@name, "password")]').send_keys(locators.password)
    sleep(0.3)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.3)
    sleep(0.3)
    print(f'LogIn to {locators.username} account at {datetime.datetime.now()}')


def TearDown():
    if driver is not None:
        print(f'_________________Test finished successfully at {datetime.datetime.now()}_________________')
        sleep(2)
        driver.close()
        driver.quit()

        logger('delleted')


def Checking_homepage_texts():
    if driver.find_element(By.XPATH, '//*[@id="speakersTxt"]').is_displayed():
        print('text: SPEAKERS is displayed')
        sleep(0.3)
    if driver.find_element(By.XPATH, '//*[@id="tabletsTxt"]').is_displayed():
        print('text: TABLETS is displayed')
        sleep(0.3)
    if driver.find_element(By.XPATH, '//*[@id="headphonesTxt"]').is_displayed():
        print('text: HEADPHONES is displayed')
        sleep(0.3)
    if driver.find_element(By.XPATH, '//*[@id="laptopsTxt"]').is_displayed():
        print('text: LAPTOPS is displayed')
        sleep(0.3)
    if driver.find_element(By.XPATH, '//*[@id="miceTxt"]').is_displayed():
        print('text: MICE is displayed')
        sleep(0.3)


def links_top_nav_menu_and_logo():
    driver.find_element(By.XPATH, "//a[normalize-space()='CONTACT US']").click()
    assert driver.find_element(By.XPATH, "//h1[normalize-space()='CONTACT US']").is_displayed()
    sleep(0.3)
    driver.find_element(By.XPATH, "//a[normalize-space()='POPULAR ITEMS']").click()
    assert driver.find_element(By.XPATH, "//h3[normalize-space()='POPULAR ITEMS']").is_displayed()
    sleep(0.3)
    driver.find_element(By.XPATH, "//a[normalize-space()='SPECIAL OFFER']").click()
    assert driver.find_element(By.XPATH, "//h3[normalize-space()='SPECIAL OFFER']").is_displayed()
    sleep(0.3)
    print('SPECIAL OFFER, POPULAR ITEMS and CONTACT US  links at the top navigation menu are clickable')
    assert driver.find_element(By.XPATH, '//span[normalize-space()="dvantage"]').is_displayed()
    print('Main logo is displayed')
    sleep(0.3)


def Check_Social_Media_links():
    assert driver.find_element(By.XPATH, "//h3[normalize-space()='FOLLOW US']").is_displayed()
    print('FOLLOW US is displayed')
    sleep(0.3)
    driver.find_element(By.XPATH, "//img[@name='follow_facebook']").click()
    handles = driver.window_handles
    newhandle = handles[1]
    driver.switch_to.window(newhandle)
    assert driver.current_url == "https://www.facebook.com/MicroFocus/"
    print('<facebook> link is clickable')
    sleep(1)
    driver.close()
    driver.switch_to.window(handles[0])
    # ______________________________________________________________________
    driver.find_element(By.XPATH,"//img[@name='follow_twitter']").click()
    handles = driver.window_handles
    newhandle = handles[1]
    driver.switch_to.window(newhandle)
    assert driver.current_url == "https://twitter.com/MicroFocus"
    print('<twitter> link is clickable')
    driver.close()
    sleep(1)
    driver.switch_to.window(handles[0])
    # ______________________________________________________________________
    assert driver.find_element(By.XPATH, "//img[@name='follow_linkedin']").is_enabled()
    print('<linkedin> link is clickable')


def Check_CONTACT_US():
    driver.find_element(By.XPATH, "//input[@name='emailContactUs']").send_keys(locators.email)
    sleep(0.3)
    driver.find_element(By.XPATH, "// textarea[ @ name = 'subjectTextareaContactUs']").send_keys(locators.subject)
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="send_btnundefined"]').click()
    sleep(0.3)
    assert driver.find_element(By.XPATH, "//p[@class='roboto-regular successMessage ng-binding']").is_displayed()
    print('Thank you for contacting Advantage support confirmation is displayed')
    sleep(0.3)
    assert driver.find_element(By.XPATH, "//a[normalize-space()='CONTINUE SHOPPING']").is_displayed()
    sleep(0.3)
    print('CONTINUE SHOPPING button is displayed')
    driver.find_element(By.XPATH, "//a[normalize-space()='CONTINUE SHOPPING']").click()
    sleep(0.3)
    print('CONTINUE SHOPPING button is clickable') #?
    print('__________________________________________________________________________________________')


def logger(action: object):
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


# SetUp()
# CrtNwAcnt()
# log_out()
# Login()
# log_out()
# Checking_homepage_texts()
# links_top_nav_menu_and_logo()
# Check_CONTACT_US()
# Check_Social_Media_links()
# TearDown()
