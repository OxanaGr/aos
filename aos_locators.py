from faker import Faker
fake = Faker(locale='en_CA')
email = fake.email()
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
phone_number = fake.phone_number()
city = fake.city()
address = fake.street_address()
province = fake.province()[:3]
username = f'{first_name}{last_name}'[:15]
postal_code = fake.postalcode()
subject = 'I Like it!'
url = 'https://advantageonlineshopping.com/#/product/'

main_page = 'https://advantageonlineshopping.com/'
title = 'Advantage Shopping'