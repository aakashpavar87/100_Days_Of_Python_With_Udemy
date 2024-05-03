import lxml
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
import random

products_info = [
    {
    "base_price": 61000,
    "url": "https://www.amazon.in/HP-Victus-Processor-Graphics-15-fa0070TX/dp/B0B74ZY9R1/ref=mp_s_a_1_5?crid" \
      "=3H4KOCHMCBKWW&keywords=hp+victus+laptop&qid=1702118890&sprefix=hp+victus+laptop%2Caps%2C338&sr=8-5"
    },
    {
        "base_price": 18000,
        "url": "https://www.amazon.in/dp/B09WQYFLRX?ref_=cm_sw_r_cp_ud_dp_JVVCB9MXJVVV79F7DAHM"
    },
    {
        "base_price": 1100,
        "url": "https://www.amazon.in/boAt-Airdopes-Atom-81-Wireless/dp/B0BKG83BTB/ref=sr_1_6?crid=2KHB2I08THJCY&"
               "keywords=boat%2Bearbuds&qid=1702123684&s=electronics&sprefix=boat%2B%2Celectronics%2C363&sr=1-6&th=1"
    }
]
my_mail = "aakashpavar87@gmail.com"
my_pass = "cwdfzwgskdqvquwf"
my_product = random.choice(products_info)
URL = my_product["url"]
base_price = my_product["base_price"]
custom = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) A"
              "ppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,gu;q=0.7"
}


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    # to store proxies

    proxies = []

    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    print(proxies)
    print(URL, base_price)
    return proxies

proxies = get_free_proxies()


def scrap_product():
    for i in range(len(proxies)):
        #printing req number
        print("Request Number : " + str(i+1))
        proxy = proxies[i]
        try:
            # response = requests.get(URL, proxies={"http": proxy, "https": proxy})
            response = requests.get(url=URL, headers=custom, proxies={"http": proxy, "https": proxy}).content
            soup = BeautifulSoup(response, "lxml")
        except:
            # if the proxy Ip is pre occupied
            print("Not Available")
        else:
            price = soup.find("div", attrs={
                "class": "a-section a-spacing-none aok-align-center aok-relative"}).find_all(
                name="span",
                attrs={"class": "a-price-whole"}
            )[0].getText()
            name = soup.find("span", id="productTitle").getText()
            return {
                "price": int(price.replace(",", "")),
                "name": name
            }


product = scrap_product()
if product["price"] is not None:
    if product["price"] < base_price:
        message = f"{product['name']}\nNow Price : {product['price']}"
        with SMTP(host="smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=my_mail, password=my_pass)
            conn.sendmail(from_addr=my_mail, to_addrs=my_mail, msg=message)
        print(product)
        print("Email Sent Successfully")
else:
    print("Sorry something went wrong")
