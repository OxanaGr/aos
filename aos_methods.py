from selenium import webdriver
import aos_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import sys
import random

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


def create_new_del_account():
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
    print(f'Password is: {locators.password}')
    print('__________________________________________________________________________________________')


def log_out():
    driver.find_element(By.ID, 'menuUserLink').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    sleep(0.6)
    print(f'Log out at {datetime.datetime.now()}')
    print('__________________________________________________________________________________________')


def login():
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


def checking_homepage_texts():
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


def check_social_media_links():
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
    print('__________________________________________________________________________________________')


def my_order():
    driver.find_element(By.XPATH, "//a[@id='hrefUserIcon']//*[name()='svg']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, "//label[@role='link'][normalize-space()='My orders']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, "//a[@class='remove red ng-scope']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, "//label[normalize-space()=', CANCEL']").click()
    sleep(0.3)
    assert driver.find_element(By.XPATH,"//span[normalize-space()='dvantage']").is_displayed()
    print('- No orders - is displayed')


def check_contact_us():
    driver.find_element(By.XPATH, "//input[@name='emailContactUs']").send_keys(locators.email)
    sleep(0.3)
    driver.find_element(By.XPATH, "// textarea[ @ name = 'subjectTextareaContactUs']").send_keys(locators.subject)
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="send_btnundefined"]').click()
    sleep(1)
    assert driver.find_element(By.XPATH, "//p[@class='roboto-regular successMessage ng-binding']").is_displayed()
    print('Thank you for contacting Advantage support confirmation is displayed')
    sleep(0.3)
    assert driver.find_element(By.XPATH, "//a[normalize-space()='CONTINUE SHOPPING']").is_enabled()
    sleep(0.3)
    driver.find_element(By.XPATH, "//a[@class='a-button ng-binding']").click()
    print('CONTINUE SHOPPING button is displayed and clickable')
    print('__________________________________________________________________________________________')


def del_account():
    driver.find_element(By.XPATH, "//a[@id='hrefUserIcon']//*[name()='svg']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, "//label[@role='link'][normalize-space()='My account']").click()
    sleep(0.3)
    full_name = driver.find_element(By.XPATH, '//*[@id="myAccountContainer"]/div[1]/div/div[1]/label').text
    print(f'Account holder is: {full_name}')
    driver.find_element(By.XPATH, "//div[@class='deleteBtnText']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, "//div[@class='deletePopupBtn deleteRed']").click()
    sleep(0.3)
    driver.get(' https://advantageonlineshopping.com/')
    sleep(0.3)
    driver.find_element(By.XPATH, "//*[name()='path' and @id='menuUserSVGPath']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(locators.username)
    sleep(0.3)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(locators.password)
    sleep(0.6)
    driver.find_element(By.XPATH, '//*[@id="sign_in_btnundefined"]').click()
    sleep(0.6)
    assert driver.find_element(By.XPATH,"//label[@id='signInResultMessage']").is_displayed()
    sleep(0.6)
    print(f'<Incorrect user name or password>. error label is displayed')
    print('Delete Account, Validate Account Deleted tests passed successfully!')
    print('__________________________________________________________________________________________')


def checkout_shopping_cart():
    n = random.choice(range(1, 34))
    if n == 13:
        n = 5
    driver.get(f'{locators.url}{n}')
    sleep(0.3)
    driver.find_element(By.XPATH, "//button[@name='save_to_cart']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="menuCart"]').click()
    sleep(0.3)
    name_of_product = driver.find_element(By.XPATH,"// label[ @class ='roboto-regular productName ng-binding']").text
    print(f'Product: {name_of_product} is added to Shopping Cart')
    driver.find_element(By.XPATH, "//button[@id='checkOutButton']").click()
    sleep(0.3)
    driver.find_element(By.XPATH, "//button[@id='next_btn']").click()
    sleep(0.2)
    driver.find_element(By.XPATH, "//input[@name='safepay_username']").send_keys(locators.username)
    sleep(0.2)
    driver.find_element(By.XPATH, "//input[@name='safepay_password']").send_keys(locators.password)
    sleep(0.2)
    driver.find_element(By.XPATH, "//button[@id='pay_now_btn_SAFEPAY']").click()
    sleep(0.3)
    sleep(0.3)
    order_info = driver.find_element(By.XPATH, '//*[@id="orderPaymentSuccess"]').text
    print(f'ORDER PAYMENT information: {order_info}')
    print('Checkout Shopping Cart Test passed Successfully!!! Yay!!!')
    sleep(0.3)
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
# create_new_del_account()
# log_out()
# login()
# checkout_shopping_cart()
# log_out()
# checking_homepage_texts()
# check_contact_us()
# links_top_nav_menu_and_logo()
# check_social_media_links()
# login()
# my_order()
# del_account()
# TearDown()
