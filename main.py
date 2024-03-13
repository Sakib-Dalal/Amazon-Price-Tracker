import requests
import smtplib
from datetime import datetime
from bs4 import BeautifulSoup

EMAIL = "sakibdalal73@gmail.com"
PASSWORD = "dzywnwnzhutsgcge"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

PRODUCT_URL = "https://www.amazon.in/gp/product/B0CN1PCYPC/ref=sw_img_1?smid=A11SUS3X5513OU&psc=1"
TARGET_PRICE = 500.0

header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

current_price = 0.0
title = ""


def source():
    response = requests.get(url=PRODUCT_URL, headers=header)
    soup = BeautifulSoup(response.text, "lxml")
    global current_price, title, link
    try:
        current_price = float(soup.find(class_='a-offscreen').get_text().split('₹')[1])
        title = soup.find(id='productTitle').get_text().strip()
    except AttributeError:
        source()


def send_email(price, title, link):
    message = f"Subject:Price Drop\n\n{title} is now Rs.{price} \nlink to buy:- {link}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=message)


while True:
    time = datetime.now().time().strftime('%H%M%S')
    if time == '090000':
        source()
        if current_price <= TARGET_PRICE:
            print(f"{current_price} Yes to buy {title}\n")
            send_email(price=current_price, title=title, link=PRODUCT_URL)
        else:
            pass

