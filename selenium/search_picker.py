#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pdb, random
 
#create an instance of the driver
driver = webdriver.Firefox()

#set implicit wait
driver.implicitly_wait(20)
 
#start using the driver, call maximize and nav to -> Google
driver.maximize_window()
driver.get('https://google.com')
 
#create a search array and extend it to include three words
search = []; search.extend( ["Superman", "Batman", "Ironman"] )
 
#randomize the word used in the Google search
random.shuffle(search)
search_field = driver.find_element_by_id('lst-ib')
search_field.send_keys('{0}'.format(*search))
 
#make a predicitive text selection (the second selection)
selections = driver.find_elements_by_class_name('sbqs_c')
for selection in selections:
  if selection == selections[1]:
    search_term = selection.text
    selection.click()

#validation step -> loop the search results, verify at least 5 results include one word from the search
results = []; search_results = driver.find_elements_by_class_name('r')
for search_result in search_results:
  search_term   = search_term.lower().split()[0]
  search_result = search_result.text.lower()
  if search_term in search_result:
    results.append(search_result)
    print ':: debug :: {0} does included the search term: {1}'.format(search_result,search_term)
assert(len(results) >= 5)
driver.close()