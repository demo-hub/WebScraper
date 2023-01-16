import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver

# Creating the .env file path
dotenv_path = os.path.abspath('.env')

# Load environment variables
load_dotenv()

# Read environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# Desired URL
url = 'https://www.continente.pt/'

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

# Maximize window
driver.maximize_window()

# Accept cookies
cookies = driver.find_element('id',
                              'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
cookies.click()

# Click logo
logo = driver.find_element('class name', 'header-logo')
logo.click()

# Clicking login button
login = driver.find_element('id', 'headerLoginForm')
login.click()

# Inserting email
email_field = driver.find_element('id', 'login-form-email-modal')
email_field.send_keys(email)

# Inserting password
password_field = driver.find_element('id', 'login-form-password-modal')
password_field.send_keys(password)

# Clicking login button
login_button = driver.find_element(
    'css selector', '.submit-login')
login_button.click()
