import requests
import os
import lxml
from bs4 import BeautifulSoup

# define headers so Amazon doesn't think you're a robot
HEADERS = {
    "User-Agent": os.environ["USER_AGENT"],
    "Accept-Language": "en-US,en;q=0.9"
}

# request to see data for amazon product
amazon_webpage_data = requests.get("https://www.amazon.com/Headphones-Cancelling-Transparency-Bluetooth-Headphones/dp/B08PZD76NP/ref=sr_1_1_sspa?crid=2TEGG0RLMIYZG&keywords=apple+headphones&qid=1699128729&s=electronics&sprefix=apple+%2Celectronics%2C136&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1", headers=HEADERS).text
# print(amazon_webpage_data)

# extract price of product
soup = BeautifulSoup(amazon_webpage_data, "lxml")
dollar_amt = soup.find(name="span", class_="a-price-whole").getText()
cent_amt = soup.find(name="span", class_="a-price-fraction").getText()
price = float(dollar_amt + cent_amt)
print(price)
