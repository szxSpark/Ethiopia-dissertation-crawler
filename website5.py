from selenium import webdriver

def crawler():
    browser = webdriver.Chrome()
    browser.get('http://www.oromooliterature.com/')
    pre = browser.find_element_by_tag_name("pre")
    p = pre.find_element_by_tag_name("p")
    news_list = []
    news_list.append(p.text)
    driver = webdriver.Chrome()
    url_set = set()
    ul = browser.find_elements_by_class_name("sub-menu")
    for i in ul:
        li = i.find_elements_by_tag_name('li')
        for j in li:
            url = j.find_element_by_tag_name('a').get_attribute('href')
            url_set.add(url)
    print(len(url_set))
    for i in enumerate(url_set):
        print(i)

    k = 0
    for url in url_set:
        print(url)
        try:
            driver.get(url)
            news_text = ''
            try:
                p = driver.find_elements_by_tag_name('p')
                for pp in p:
                    if pp.get_attribute('class') == None or pp.get_attribute('class') == '':
                        news_text += pp.text + '\n'
                print(k)
                k += 1
                print(news_text)
                news_list.append(news_text)
            except BaseException as e:
                print("该页无p")
        except BaseException as e:
            print("连接超时")
    print(len(news_list))
    driver.close()
    browser.close()
    return news_list
