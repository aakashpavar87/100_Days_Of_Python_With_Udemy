# import requests
# import lxml
# from bs4 import BeautifulSoup
# # URL = "https://www.amazon.in/dp/B09WQYFLRX?ref_=cm_sw_r_cp_ud_dp_GAZ56P5BZ7HQVQZD66BC_1&th=1"
# URL = "https://www.amazon.in/HP-Victus-Processor-Graphics-15-fa0070TX/dp/B0B74ZY9R1/ref=mp_s_a_1_5?crid" \
#       "=3H4KOCHMCBKWW&keywords=hp+victus+laptop&qid=1702118890&sprefix=hp+victus+laptop%2Caps%2C338&sr=8-5"
# custom = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) A"
#               "ppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,gu;q=0.7"
# }
#
# def get_free_proxies():
#     url = "https://free-proxy-list.net/"
#     # request and grab content
#     soup = BeautifulSoup(requests.get(url).content, 'html.parser')
#     # to store proxies
#     proxies = []
#     for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
#         tds = row.find_all("td")
#         try:
#             ip = tds[0].text.strip()
#             port = tds[1].text.strip()
#             proxies.append(str(ip) + ":" + str(port))
#         except IndexError:
#             continue
#     return proxies
#
# # url = "http://httpbin.org/ip"
#
# proxies = get_free_proxies()
#
# for i in range(len(proxies)):
#
#     #printing req number
#     print("Request Number : " + str(i+1))
#     proxy = proxies[i]
#     try:
#         # response = requests.get(URL, proxies={"http": proxy, "https": proxy})
#         response = requests.get(url=URL, headers=custom, proxies={"http": proxy, "https": proxy}).content
#         soup = BeautifulSoup(response, "lxml")
#     except:
#         # if the proxy Ip is pre occupied
#         print("Not Available")
#     else:
#         print(soup.find("div", attrs={"class": "a-section a-spacing-none aok-align-center aok-relative"})
#               .find_all("span", attrs={"class": "a-price-whole"}))
#         break
#
# # response = requests.get(url=URL, headers=custom).content
#
#
print(int(("17,990").replace(",", "")))
