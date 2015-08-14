#!/usr/bin/env python

from selenium import webdriver
import datetime
import json
import sys
import time
import selenium
from getpass import getuser
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


comp_user = getuser()
if comp_user == "aashiq":
    user = "aashiq.d@gmail.com"
    pw = "C!hmTWYR9Zk"
elif comp_user =="James":
    user = "jtanman@gmail.com"
    pw = "%t39XqV0dGp&"
    dirname = "C:\Users\James\Dropbox\Pappy\\"
elif comp_user == 'christiandrappi':
    dirname = "/Users/christiandrappi/Dropbox/Pappy/"



def load_browser():
    br = webdriver.Chrome()
    br.get("https://www.couchsurfing.com/")
    #br.execute_script('closeAgePopupBlock("ageVerify")')
    return br

def login(br):
    br.find_element_by_xpath("//a[contains(@href,'users/sign_in')]").click()
    #br.find_element_by_href("/users/sign_in").click()
    br.implicitly_wait(10)
    user_field = br.find_element_by_name("user[login]")
    user_field.send_keys(user)
    pw_field = br.find_element_by_name("user[password]")
    pw_field.send_keys(pw)

    br.find_element_by_name("commit").click()



    

def list_people(br):
    people = br.find_link_by_partial_href("/people")
    print(people)
    return people

def send_message(people_id, br):
    people_id.click()
    br.find_link_by_partial_href("/couch_visits").click()
    




def buy_spirit(br, spirit):
    br.fill("SearchKeyWord", spirit)
    br.find_by_id('goSpiritButton').first.click()
    all_products = br.find_link_by_partial_href("SpiritsProductDisplayView")
    ap_text = [p.text for p in all_products if p.text != u'More']

    try:
        match_pos = [verify_vintage(spirit, text) for text in ap_text].index(True)
    except ValueError:
        return False

    try:
        br.execute_script('Add2ShopCart(document.OrderItemAddForma%g)'%match_pos)
        try:
            br.find_by_id('quickcheckOut').first.click()
        except:
            br.find_by_id('checkOut').first.click()
            login(br)
            br.find_by_id('quickcheckOut').first.click()
        br.find_by_id('submitOrder').first.click()
        return True
    except:
        return False

# <input type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" class="select2-input" role="combobox" aria-expanded="true" aria-autocomplete="list" aria-owns="select2-results-1" id="s2id_autogen1_search" placeholder="">

def search_city(br):
    city = "Tokyo"
    # br.find_by_id("s2id_autogen2_search").click()
    # city_box = br.find_element_by_id("s2id_search_query")
    # city_box.click()
    # input_box = br.find_element_by_class_name("select2-input")
    # input_box.send_keys(city)


    # br.find_element_by_class_name("select2-results-dept-0.select2-result.select2-result-selectable").click()

    el = br.find_element_by_id('s2id_search_query')
    actions = ActionChains(br)
    actions.move_to_element(el)
    actions.click()
    actions.send_keys(city)
    actions.perform()


    # <li class="select2-results-dept-0 select2-result select2-result-selectable" role="presentation"><div class="select2-result-label" id="select2-result-label-7" role="option"><span class="select2-match">Tokyo</span>, Japan</div></li>

    item_to_select = "Tokyo"

    # xpath = '//div[@class="select2-results-dept-0.select2-result.select2-result-selectable" and' +\
    #     ' text()[contains(.,"%s")]]' % (item_to_select)

    xpath = '//div[@class="select2-result-label" and' +\
        ' text()[contains(.,"%s")]]' % (item_to_select)    

    wait = WebDriverWait(br, 10)
    elm = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                xpath
            )
        ),
        'waiting for %s to be clickable' % (xpath)
    )
    elm.click()

    # br.implicitly_wait(10)
    # br.find_element_by_class_name("select2-hidden-accessible").click()
    # select.select_by_visible_text('Tokyo, Japan')

    # br.get("https://www.couchsurfing.com/members/hosts?utf8=\xe2&search_type=host&search_query=Tokyo%2CJapan&latitude=35.6894875&longitude=139.6917064&country=Japan&region=Tokyo")


    # br.implicitly_wait(10)
    # input_box.send_keys(Keys.RETURN)
    #br.find_element_by_id("s2id_search_query").click()
    # # br.type("Tokyo, Japan")
    
    # city_box.send_keys("Tokyo, Japan")

    # br.fill("search_query", "Tokyo, Japan")

    # search_box = br.find_element_by_name("search_query")
    # search_box.click()



    # br.fill("s2id_search_query", "Tokyo, Japan")
    # br.type("search_query", "Tokyo, Japan", slowly = True)
    # br.type("search_query", "Tokyo, Japan")
    # b.execute_script('document.getElementsByName("f")[0].submit()')

    # try:
    #     br.find_by_id('s2id_autogen1_search').fill("Tokyo")
    # except: 
    #     try:
    #         br.visit("https://www.finewineandgoodspirits.com")
    #         login(br)
    #     except:
    #         alert = br.switch_to_alert()
    #         alert.dismiss()
    #         br.visit("https://www.finewineandgoodspirits.com")
    #         login(br)
    #     return(False)

    # try:
    #     br.find_by_id('goSpiritButton').first.click()
    #     has_pappy = br.is_element_present_by_id("productList")
    # except:
    #     try:
    #         alert = br.switch_to_alert()
    #         alert.dismiss()
    #     except:
    #         br.visit("https://www.finewineandgoodspirits.com")
    #         login(br)
    #     return False
    # return has_pappy




# products = [["Pappy Van Winkle 23", False], ["Pappy Van Winkle 20", False], ["Pappy Van Winkle 15", False]]







if __name__ == '__main__':
    br = load_browser()
    login(br)
    search_city(br)
    # while run_pappy(products):

    #     if(numPurchases >= 3):
    #         break

    #     if check_pappy(br):
    #         for i,p in enumerate(products):
    #             if not(products[i][1]):
    #                 if buy_spirit(br, p[0]):
    #                     numPurchases = numPurchases + 1
    #                     products[i][1] = True
    #                     ts = datetime.datetime.now()                        
    #                     f.write("\n" + str(ts) + " bought " + products[i][0] + "\n")
    #                     f.flush()
    #     else:
    #         ts = datetime.datetime.now()
    #         if ts.minute != last_min:
    #             f.write(str(ts) + " no pappy\n")
    #             last_min = ts.minute
    #             f.flush()

    #     # print("sleeps")
    #     time.sleep(1.0)
    # ts = datetime.datetime.now()
    # f.write("\n" + str(ts) + " done buying pappy!")


