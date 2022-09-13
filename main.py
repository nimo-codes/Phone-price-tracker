import playsound
import requests
from bs4 import BeautifulSoup
import smtplib
import keyring
import time as tt

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("namannanda5657@gmail.com", keyring.get_password("mail", "namannanda5657"))
    subject = "price is less than 65000"
    body = "the link is "
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        "namannanda5657@gmail.com",
        "lifelovesnaman@gmail.com",
        msg 
    )
    print("mail sent!!")
    server.quit()

def check():
    print("         CHECKING       ")
    url = "https://www.amazon.in/iPhone-14-128GB-Product-RED/dp/B0BDJVSDMY/ref=sr_1_3?crid=RHAGKA1A1FVA&keywords=iphone+14&qid=1663097462&sprefix=iphone+1%2Caps%2C280&sr=8-3"
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15",
        "Accept-Encoding": None 
    }

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text,'html.parser')
    name = soup.find(id = "productTitle").get_text()
    name = name[1:31]
    name = name.lstrip()
    price = soup.find(class_ = "a-offscreen").get_text()
    price1 = price[1:3]
    price2 = price[4:7]
    price = int(price1 +price2)
    
    if price <= 65000:
        send_mail()
        quit

    else:
        print(f"{name}:{price}")

while True:

    check()
    print("\n")
    print("checking price again in 10 seconds....")
    playsound("/Users/jarvis/pymycod/automation/beep-02.mp3")
    print("\n")
    tt.sleep(10)
    




    


