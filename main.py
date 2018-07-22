"""
Summer, 2018
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fake_email_gen import rand_email
import sys

# Take number of votes the is to be submitted. Default value is 50
if len(sys.argv) < 2:
    num_votes = 50
else:
    num_votes = int(sys.argv[1])

# file with the URL for specific intern account page
f = open('creds.txt')
url = f.read()
chrome_path = r"C:\Users\jzerez\Desktop\chromedriver_win32\chromedriver.exe"
successful_votes = 0

for i in range(num_votes):
    """
    This really should be handled better than just wrapping everything in a
    try-except, but there are often unforseeable errors that can arise with
    Selenium, and as such, it is hard to catch all of them. :(
    """
    try:
        # Initializes the webdriver instance to run on Chromium
        driver = webdriver.Chrome(chrome_path)
        driver.get(url)
        driver.implicitly_wait(1)

        # Locates the vote button, navigates to the vote button, waits, then pushes the vote button.
        vote_button = WebDriverWait(driver, 3000).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="my_db_entry_193788153"]/div[3]'))
        )
        webdriver.ActionChains(driver).move_to_element(vote_button)
        webdriver.ActionChains(driver).perform()
        time.sleep(1.5)
        webdriver.ActionChains(driver).click(vote_button).perform()
        time.sleep(1.5)

        # Wait until a specific header object that corresponds to the email page is found
        header = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content_rich_text5"]/h1'))
        )
        # Generate fake user details
        first_name, last_name, email = rand_email()

        # find input fields
        first_name_element = driver.find_elements_by_id('form3_first_name')
        last_name_element = driver.find_elements_by_id('form3_last_name')
        email_element = driver.find_elements_by_id('form3_email')
        checkbox_element = driver.find_elements_by_id('form3_custom_field_5_block')
        submit_element = driver.find_elements_by_id('form3_submit_block')

        # Push fake user details to appropriate fields
        first_name_element[0].send_keys(first_name)
        last_name_element[0].send_keys(last_name)
        email_element[0].send_keys(email)
        # move to the checkbox, wait, then click it.
        webdriver.ActionChains(driver).move_to_element(checkbox_element[0])
        webdriver.ActionChains(driver).perform()
        time.sleep(0.5)
        webdriver.ActionChains(driver).click(checkbox_element[0]).perform()
        submit_element[0].click()

        # keep track of number of successful votes.
        successful_votes += 1
        driver.quit()
    except:
        pass
# final information about the success of the program.
print(successful_votes, 'votes successful out of', num_votes)
