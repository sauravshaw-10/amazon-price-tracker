import requests
import smtplib
from bs4 import BeautifulSoup
import lxml

MY_EMAIL = "saurav.shaw10@gmail.com"
MY_PASSWORD = "qwxuglkmnyysjbgp"
TARGET_PRICE = 900
URL = "https://www.amazon.in/Oliveware-Teso-Lunch-Box-Bottle/dp/B08CRVJZKS/"

params = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=params)
soup = BeautifulSoup(response.text, "lxml")

# print(soup.prettify())

price = soup.find(name="span", class_="a-price-whole")
item_price = float(price.getText())
detail = soup.find(name="span", id="productTitle")
item_details = detail.getText().strip().replace("|", ",")


#------------------EMAIL-ALERT--------------------#

if item_price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Amazon Price Alert!\n\n{item_details} is now at ₹{item_price}. Buy now!\n{URL}".encode("utf-8")
                            )




