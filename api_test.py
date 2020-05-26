import requests
import random

emails = ['@gmail.com', '@outlook.com', '@outlook.be', '@sgsintpaulus.eu', '@hotmail.com', '@telenet.be']
emailadres = '{}.{}{}'

def get_email():
    r = requests.get('https://randomuser.me/api/')
    preview = r.json()

    data = preview['results'][0]['name']

    voornaam = data['first']
    achternaam = data['last']

    server = random.choice(emails)
    print(emailadres.format(voornaam, achternaam, server))


def get_pw():
    r = requests.get('https://randomuser.me/api/')
    preview = r.json()['results'][0]['login']['username']

    return preview

for i in range(10):
    print(get_pw())