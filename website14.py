from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def crawler():
    browser = webdriver.Chrome()
    browser.get('http://www.gadaa.com/')
    driver = webdriver.Chrome()
    news_list = []
    for i in browser.find_elements_by_xpath("//h2/a[@href]"):
        try:
            url = i.get_attribute('href')
            driver.get(url)
        except BaseException as e:
            print(e)
        try:
            nachricht = driver.find_element_by_class_name('postentry').text
            if len(nachricht) > 10:
                print(nachricht)
                news_list.append(nachricht)
            else:
                print("short news", len(nachricht))
        except BaseException as e:
            print("该页无新闻")
    print(len(news_list))
    driver.close()
    browser.close()
    return news_list

crawler()

