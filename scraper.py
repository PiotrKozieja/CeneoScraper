import requests
from bs4 import BeautifulSoup
product_code = "100842555"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
response =requests.get(url)
page_dom = BeautifulSoup(response.text,"html.parser")
opinions = page_dom.select("div.js_product-review")
print(url)
print(type(page_dom))
print(type(opinions))
print(len(opinions))

#print(page_dom.prettify())