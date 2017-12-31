#encode = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def crawler_write():
    browser = webdriver.Chrome()
    browser.get('http://www.oromiyaa.gov.et')
    file = open("./news/Thread-13_oromiyaa.gov.et.txt", 'w', encoding= 'utf-8')
    nachricht = ""
    for i in  browser.find_elements_by_xpath("//div[@class='journal-content-article']/pre"):
       text = i.text
       text = text.replace('\n',' ')
       nachricht = nachricht+text
    #file.write(nachricht)
    driver = webdriver.Chrome()
    for page in range(2,6):
        url = 'http://www.oromiyaa.gov.et/web/guest/home?p_p_id=56_INSTANCE_XS5w&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=4&page='+str(page)
        driver.get(url)
        print(url)
        for link in driver.find_elements_by_xpath("//div[@class='journal-content-article']/span|//div[@class='journal-content-article']/p"):
            text = link.text.replace('\n', ' ')
            nachricht += text+"\n"
    print(nachricht)
    file.write(nachricht)
    file.close()
    driver.close()
    browser.close()

crawler_write()