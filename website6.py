from selenium import webdriver

def crawler():
    '''
    meta-image
    '''
    website = ['https://www.opride.com/afaan-oromo/', 'https://www.opride.com/afaan-oromo/page/2/', 'https://www.opride.com/afaan-oromo/page/3/']
    url_set = set()
    browser = webdriver.Chrome()
    for wb in website:
        browser.get(wb)
        div = browser.find_elements_by_class_name("meta-image")
        for divv in div:
            url = divv.find_element_by_tag_name("a").get_attribute("href")
            url_set.add(url)

    news_list = []
    print(len(url_set))
    driver = webdriver.Chrome()
    k = 0
    for url in url_set:
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

    print(len(news_list))
    browser.close()
    driver.close()
    return news_list

