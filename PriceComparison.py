from bs4 import BeautifulSoup
import requests

product="iphone 11"
#product=input("enter a product name: ")
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

def replacer(product):
    return product.replace(" ","+")

def hepsiburada(product):
    url="https://www.hepsiburada.com/ara?q="+replacer(product)
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.text,"html.parser")
    table=soup.find_all("div",{"class":"contain-lg-3 contain-md-3 contain-sm-3 fluid with-bottom-border"})
    table=table[0]
    table=((table.find_all("ul"))[0])
    table=(table.find_all("a"))
    item=table[0]
    item_info=(item.find_all("div",{"class":"product-detail"}))
    item_info=item_info[0]
    extra_discount=item_info.find_all("div",{"class":"price-value"})
    if len(extra_discount)>0:
        print((extra_discount[0].text).replace(" ",""))
    else:
        price=item_info.find_all("span",{"class":"price product-price"})
        print(price[0].text)

def amazon(product):
    url="https://www.amazon.com.tr/s?k="+replacer(product)
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,"html.parser")
    table=soup.find_all("div",{"class":"s-main-slot s-result-list s-search-results sg-row"})
    item=table[0].find_all("div",{"data-index":1})[0]
    item_price=item.find_all("div",{"class":"a-section a-spacing-none a-spacing-top-small"})
    item_price=item_price[1].find_all("span",{"class":"a-offscreen"})
    print(item_price[0].text)

def trendyol(product):
    url="https://www.trendyol.com/sr?q="+replacer(product)
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,"html.parser")
    table=soup.find_all("div",{"class":"prdct-cntnr-wrppr"})
    item=table[0].contents[0]
    item=item.find_all("div",{"class":"p-card-chldrn-cntnr"})
    item=item[0].contents[0]
    item=item.find_all("div",{"class":"prmtn-cntnr"})
    print(item[0].text)

def n11(product):
    url="https://www.n11.com/arama?q="+replacer(product)
    r=requests.get(url)
    soup= BeautifulSoup(r.content,"html.parser")
    table=soup.find_all("li",{"class":"column"})
    table=table[0]
    table=table.find_all("ins")
    price=(table[0].text)
    price= price.replace("\n","")
    price= price.replace(" ","")
    print(price)

print("***************n11*********************")
n11(product)
print("**************hepsiburada*************")
hepsiburada(product)
print("****************trendyol**************")
trendyol(product)
print("****************amazon**************")
amazon(product)