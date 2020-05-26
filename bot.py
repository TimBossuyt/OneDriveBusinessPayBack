from selenium import webdriver
import requests
import random
import time

emails = ['@gmail.com', '@outlook.com', '@outlook.be', '@sgsintpaulus.eu', '@hotmail.com', '@telenet.be']
emailadres_raw = '{}.{}{}'

def get_email():
    r = requests.get('https://randomuser.me/api/')
    preview = r.json()

    data = preview['results'][0]['name']

    voornaam = data['first']
    achternaam = data['last']

    server = random.choice(emails)
    print(emailadres_raw.format(voornaam, achternaam, server))
    return emailadres_raw.format(voornaam, achternaam, server)

def get_pw():
    r = requests.get('https://randomuser.me/api/')
    preview = r.json()['results'][0]['login']['username']
    print(preview)
    return preview

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Main loop
while True:
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSctWWooyjdGIfLxXDszphrfkeyVEh-Rj_CFJV4Y4feZn5elSA/viewform")

    form_email = driver.find_element_by_name("entry.1136939887")
    form_pw = driver.find_element_by_name("entry.1342759352")
    form_email.send_keys(get_email())
    form_pw.send_keys(get_pw())


    #Press submit button
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()

