from selenium import webdriver

def crawler():
    browser = webdriver.Chrome()
    browser.get('http://ayyaantuu.net/')
    '''
    website = http://ayyaantuu.net/
    '''
    a = browser.find_elements_by_tag_name("a")
    news_list = []
    driver = webdriver.Chrome()
    url_set = set()
    for i in a:
        if (i.get_attribute('class') == '' or i.get_attribute('class') == None )\
                and (i.get_attribute('href') != '' or i.get_attribute('href') == None):
            url = i.get_attribute('href')
            url_set.add(url)
    url_noise_set = set()
    li = browser.find_elements_by_tag_name("li")
    for i in li:
        try:
            url_noise_set.add(i.find_element_by_tag_name('a').get_attribute('href'))
        except BaseException as e:
            pass
    url_set = url_set - url_noise_set
    for url in url_set:
        if url == None:
            continue
        driver.get(url)
        news_text = ''
        try:
            p = driver.find_elements_by_tag_name('p')
            for pp in p:
                if pp.get_attribute('class') == None or pp.get_attribute('class') == '':
                    news_text += pp.text + '\n'
        except BaseException as e:
            print("该页无p")
        news_list.append(news_text)

    driver.close()
    browser.close()
    return news_list
