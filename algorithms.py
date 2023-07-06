
import sqlite3
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading


driver=webdriver.Chrome()
conn = sqlite3.connect('users3.db')
cursor = conn.cursor()


# defs static_algorithm

def static_technolife(url) :
    try :
      driver.get(url)
      time.sleep(5)
      try :
       price2=driver.find_element(By.CLASS_NAME,"ProductComp_main_price__XgWce")
       time.sleep(2)
       try :
        price1=driver.find_element(By.CLASS_NAME,"ProductComp_offer_price__HAQ6N")
        time.sleep(2)
        if int(persian_to_english(price2.text[:-5]).replace(",",""))<(1/2)*int(persian_to_english(price1.text[:-5]).replace(",","")):
          return(persian_to_english(price1.text[:-5]).replace(",",""))
        else:
           return (persian_to_english(price2.text[:-5]).replace(",",""))
       except :
        # print(va)
        # print("not found")
        return(persian_to_english(price2.text[:-5]).replace(",",""))
      except :
        price1=driver.find_element(By.CLASS_NAME,"ProductComp_offer_price__HAQ6N")
        time.sleep(2)
        return (persian_to_english(price1.text[:-5]).replace(",",""))
    except ValueError as va:
        print(va)
        # print("not found")
        return 'None'


def persian_to_english(text):
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    translation_table = str.maketrans(persian_digits, english_digits)
    return text.translate(translation_table)

def static_divar(url) :
    try:
        driver.get(url)
        time.sleep(5)
        price3=driver.find_elements(By.CLASS_NAME,"kt-post-card__description")
        time.sleep(2)
        a = persian_to_english(price3[1].text)[:-5]
        return (a)
        # print(persian_to_english(price3[1].text)[:-5])
        # return persian_to_english(price3[1].text)[:-5]
    except :
        print("not found")
        # return 'None'

def static_digikala(url) :
     try :
        driver.get(url)
        time.sleep(7)
        price2=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)")
        time.sleep(5)
        if len(price2)==0 :
            try:
                price1=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")
                time.sleep(5)
                # print(persian_to_english(price1[0].text))
                return(persian_to_english(price1[0].text))
            except :
                return (None)

        if "٪" in price2[0].text :
            if len(price2)>=2 :
                # print(persian_to_english(price2[1].text))
                return (persian_to_english(price2[1].text))
            else :
                price1=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")
                time.sleep(5)
                # print(persian_to_english(price1[0].text))
                return(persian_to_english(price1[0].text))
        else :
            return(persian_to_english(price2[0].text))

     except ValueError as va:
        print(va)
        # print("not found")
        return 'None'


# defs search_algorithm
def technolife() :
 try :
  global my_current_url
  # motor technolife

  driver.get(my_current_url)
  # tv_phone
  time.sleep(5)
  elements_search=driver.find_elements(By.CLASS_NAME,"ProductComp_product_title__bOrf5")
  time.sleep(2)
  name1=elements_search[0].text
  time.sleep(7)
  price=driver.find_element(By.CLASS_NAME,"ProductComp_main_price__XgWce")
  time.sleep(3)
  price1=price.text[:-5]
  url_i=driver.current_url
  elements_search[0].send_keys(Keys.ENTER)
  # Property=driver.find_element(By.CLASS_NAME,"product_technical__qvJms")
  driver.switch_to.window(driver.window_handles[0])
  url=driver.current_url
  Property=driver.find_element(By.ID,"ProductSpecPart")
  time.sleep(5)
  Property1=(Property.text)[:-24]

  print(Property1)
  print(url)
  print(name1)
  print(price1.replace(',',""))
  print(url_image(url_i))
 except :
     pass




def digikala() :
 try :
  global search1,price
  driver.get("https://www.digikala.com")
  time.sleep(10)
  s=driver.find_element(By.CSS_SELECTOR,".SearchInput_SearchInput__HB9qi")
  time.sleep(1)
  s.click()
  search_box=driver.find_element(By.CSS_SELECTOR,"input.color-500")
  time.sleep(5)
  search_box.send_keys(search1)
  time.sleep(3)
  search_box.send_keys(Keys.ENTER)

  # tv_phone
  time.sleep(1)
  name_product=driver.find_elements(By.CLASS_NAME,"ellipsis-2")
  time.sleep(5)
  # grantarin[0].send_keys(Keys.ENTER)
  # time.sleep(1)
  value=driver.find_elements(By.CSS_SELECTOR,"div.product-list_ProductList__item__LiiNI:nth-child(1) > a:nth-child(1) > div:nth-child(1) > article:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1)")
  time.sleep(5)
  # print(name_product[0].text)
  time.sleep(3)
  driver.switch_to.window(driver.window_handles[0])
  url=driver.current_url
  print(url)
  if "٪" in value[0].text :
   price=str(value[1].text).replace(',',"")
   print(persian_to_english(price))
  else :
    price=str(value[0].text).replace(',',"")
    print(persian_to_english(price))

  divar()
 except :
     pass




def search() :
 try :
  global my_current_url,search1

  driver.get("https://www.technolife.ir/")
  time.sleep(5)
  box_search=driver.find_element(By.CSS_SELECTOR,"#search_box")
  time.sleep(1)
  box_search.send_keys(search1)
  time.sleep(2)
  box_search.send_keys(Keys.ENTER)
  time.sleep(4)
  driver.switch_to.window(driver.window_handles[0])
  time.sleep(1)
  my_current_url=driver.current_url
  technolife()
 except :
     return(None)


def divar() :
  try :
    global search1,price

    driver.get("https://divar.ir/s/tehran")

    time.sleep(3)

    box_search=driver.find_element(By.CLASS_NAME,"kt-nav-text-field__input")
    time.sleep(3)
    box_search.send_keys(search1)
    box_search.send_keys(Keys.ENTER)
    time.sleep(2)
    current_url=driver.current_url

    url2=re.split("tehran?",str(current_url))
    min=int((6/10)*int(10000000))
    max=int((11/10)*int(10000000))
    komaki="price="+str(min)+"-"+str(max)+"&"
    new_url=url2[0]+"tehran?"+komaki+url2[1][1:]

    driver.get(new_url)
    time.sleep(5)

    values=driver.find_elements(By.CLASS_NAME,"kt-post-card__description")
    time.sleep(3)
    pricce=values[1].text
    values[0].click()
    time.sleep(4)
    time.sleep(1)
    urrl=driver.current_url
    return(urrl)
    return(persian_to_english(pricce)[:-5].replace(',',""))
  except :
      return(None)

def url_image(url) :
 try :

  driver.get(url)
  time.sleep(5)
  element = driver.find_element(By.CSS_SELECTOR,".ProductComp_product_image__JBXYv > img:nth-child(1)")
  time.sleep(4)
  myImage = element.get_attribute("src")
  print(myImage)

 except :
     print("not found")
     
search1=""

try:                            
                t1 = threading.Thread(target=search())
                t2 = threading.Thread(target=digikala())
                t1.start()
                t2.start()
                t1.join()
                t2.join()
                driver.close()
               
except ValueError as va:
                print(va)
                