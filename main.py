import requests
import os
import lxml
from bs4 import BeautifulSoup
import smtplib

# define headers so Amazon doesn't think you're a robot
HEADERS = {
    "User-Agent": os.environ["USER_AGENT"],
    "Accept-Language": "en-US,en;q=0.9"
}

# user questionnaire
email = input("What's your email? ")
url = input("Enter URL for Amazon product price you want to track: ")
desired_price = float(input("What's the lowest price you are willing to pay for the product? $"))

# request to see data for amazon product
amazon_webpage_data = requests.get(url, headers=HEADERS).text
# print(amazon_webpage_data)

soup = BeautifulSoup(amazon_webpage_data, "lxml")

# extract price of product
dollar_amt = soup.find(name="span", class_="a-price-whole").getText()
cent_amt = soup.find(name="span", class_="a-price-fraction").getText()
price = float(dollar_amt + cent_amt)

# extract product title
product_title = soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break").getText().strip()
product_title = product_title.encode("utf-8")

# check if price of item is equal to or lower than desired price  
if price <= desired_price:
    # if price is lower than desired price, send user an email alert
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL"], password=os.environ["PW"])
        connection.sendmail(
            from_addr=os.environ["EMAIL"],
            to_addrs=email,
            msg=f"Subject:Price Drop for Amazon Wishlist Item\n\nConsider buying {product_title} now! It's now ${price}. {url}"
        )