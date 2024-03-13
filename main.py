import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

PRODUCT_URL = "https://www.amazon.in/RIDEN-Raspberry-Connector-Expansion-Transparent/dp/B0CN1PCYPC/ref=sr_1_17?crid=28VYTE0WTLNUC&dib=eyJ2IjoiMSJ9.jGws0p0X_ArKMlWkQX06JCVDeJyvpoo8RiGSpzNxY4_gra_mb0JCsyJ5ujG0n9jM1W_bc177ciVMf1iEYyQbFzeaTKx5hbUSvd43Te9VLOQ4jBxaT7cV4yytR6wPdHX0j29ziTBqyaxsND2Qi6b4L0Tuif46X10G0jF5Tfv5gAjcPwWFieTFufCzdN3CGLJZrFs6mYkhawqicJH459LHLz3uOzus5AkbuhTfP5sAUJc.FUz0DnHhwN8lh9NlcGYvbPw7HlYSEN0s_ZWr-YBtbz0&dib_tag=se&keywords=raspberry+pi+zero+case&qid=1710302940&sprefix=raspberry+pi+zero+case%2Caps%2C289&sr=8-17"

header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url=PRODUCT_URL, headers=header)
soup = BeautifulSoup(response.text, "lxml")

print(soup.prettify())

