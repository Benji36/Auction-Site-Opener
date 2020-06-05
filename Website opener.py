#Website opener

import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pages = ['https://www.rbauction.com/oceania?keywords=mack&region=11754635523',  
        'https://www.pickles.com.au/trucks/item/search#!/search-result?q=(And.Make.Mack._.ProductType.Trucks.)',
        'https://www.manheim.com.au/trucks-machinery/search?Keywords=mack&PageNumber=1&RecordsPerPage=50&searchType=Z&page=1',
        'https://www.graysonline.com/automotive-trucks-and-marine/transport-trucks-and-trailers?make=mack',
        'https://www.lloydsonline.com.au/AuctionLots.aspx?kw=mack&smode=0']

#chrome_driver = 'C:\\Users\\BEN\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\site-packages\\chromedriver_win32.exe'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get(pages[0])
for i in range (1,len(pages)):
    driver.execute_script("window.open('','_blank');")
    driver.switch_to.window(driver.window_handles[i])
    try:
        driver.get(pages[i])
    except:
         continue
