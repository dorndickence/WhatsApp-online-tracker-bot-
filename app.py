from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def get_pairing_code():
    br = webdriver.Chrome()
    br.get('https://web.whatsapp.com')

    input("Press any key after entering your credentials and reaching the WhatsApp main page")
    time.sleep(10)

    pairing_code = br.find_element_by_class_name('_1yHR2').text
    return pairing_code

def find_and_send_message(contact, message):
    search = br.find_element_by_tag_name('input')
    search.send_keys(contact, Keys.ENTER)
    time.sleep(10)

    chat_input = br.find_element_by_class_name('_13mgZ')
    chat_input.send_keys(message, Keys.ENTER)

br = webdriver.Chrome()
br.get('https://web.whatsapp.com')

input("Press any key after scanning QR code")

while True:
    user_input = input("Enter the contact you want to search for (or q to quit): ")
    if user_input.lower() == 'q':
        break

    pairing_code = get_pairing_code()
    find_and_send_message(user_input, pairing_code)

br.quit()