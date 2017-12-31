from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def crawler():
    browser = webdriver.Chrome()
    browser.get('http://www.orto.et/')
    #element = browser.find_elements_by_xpath("//*[@href]")
    news_list = []
    driver = webdriver.Chrome()
    for i in browser.find_elements_by_xpath("//*[@class='portlet-body']/div/a[@href]"):
        try:
            url = i.get_attribute('href')
            driver.get(url)
            nachricht = driver.find_element_by_class_name('journal-content-article').text
            if len(nachricht) > 10:
                news_list.append(nachricht)
        except BaseException as e:
            print("该页无新闻")
    print(len(news_list))
    driver.close()
    browser.close()
    return news_list