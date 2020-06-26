import requests
from bs4 import BeautifulSoup
import smtplib, ssl

def hasStock(s):
    return any(char.isdigit() for char in s)

def sendEmail(po, c, s, pa, r, m):
    with smtplib.SMTP_SSL("smtp.gmail.com", po, context=c) as server:
        server.login(s, pa)
        server.sendmail(s, r, m)


#url of the product
url = ''

#email address of the sender
sender = ""

#password for the email address of the sender
#password = input("password: ")
password = ""

#email address of the receiver
receiver = ""

#message to be sent in the email
message = ""

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

port = 465
context = ssl.create_default_context()

#availability of the product
#example code for checking availability in certain store locations
availability = soup.select('div.c-capr-inventory-store')
for i in range(4):
    if hasStock(availability[i].text.strip().splitlines()[2]):
        sendEmail(port, context, sender, password, receiver, message)
        break
