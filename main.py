import requests
import smtplib
from datetime import datetime
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
PRODUCT_URL = "https://www.amazon.in/gp/product/B0CN1PCYPC/ref=sw_img_1?smid=A11SUS3X5513OU&psc=1"
TARGET_PRICE = 500.0

header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

current_price = 0.0
time = datetime.now().time()
print(time)

def source():
    response = requests.get(url=PRODUCT_URL, headers=header)
    soup = BeautifulSoup(response.text, "lxml")
    global current_price
    try:
        price = float(soup.find(class_='a-offscreen').get_text().split('₹')[1])
        current_price = price
    except AttributeError:
        source()

while True:
    source()
    print(current_price)
    if current_price <= TARGET_PRICE:
        print("Yess to buy")
    else:
        pass
