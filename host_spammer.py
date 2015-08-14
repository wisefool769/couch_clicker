#!/usr/bin/env python

from splinter import Browser
import datetime
import json
import sys
import time
import selenium
from getpass import getuser
from selenium.webdriver.common.alert import Alert


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

br = Browser('chrome')

def load_browser():
    # br = Browser('chrome')
    br.visit("https://www.couchsurfing.com/")
    #br.execute_script('closeAgePopupBlock("ageVerify")')
    return br

def login(br):
    try:
        br.click_link_by_href("/users/sign_in")
        br.fill("user[login]",user)
        br.fill("user[password]",pw)
        br.find_by_name("commit").click()
        # br.click_link_by_href("javascript:prepareSubmit(document.Logon)")
        # br.find_element_by_name('commit').click()
        # br.find_element_by_class_name('cs-button.pure-input-1.js-submit-login').click()   
        # br.find_element(By.XPATH, '//button[text()="Log In"]')
        # br.find_element_by_css_selector('cs_button').click()
        return None
    except:
        return None
    

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

def check_pappy(br):
    try:
        br.fill("SearchKeyWord", pappy_search)
    except: 
        try:
            br.visit("https://www.finewineandgoodspirits.com")
            login(br)
        except:
            alert = br.switch_to_alert()
            alert.dismiss()
            br.visit("https://www.finewineandgoodspirits.com")
            login(br)
        return(False)

    try:
        br.find_by_id('goSpiritButton').first.click()
        has_pappy = br.is_element_present_by_id("productList")
    except:
        try:
            alert = br.switch_to_alert()
            alert.dismiss()
        except:
            br.visit("https://www.finewineandgoodspirits.com")
            login(br)
        return False
    return has_pappy




# products = [["Pappy Van Winkle 23", False], ["Pappy Van Winkle 20", False], ["Pappy Van Winkle 15", False]]







if __name__ == '__main__':
    br = load_browser()
    login(br)
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


