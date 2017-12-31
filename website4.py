from selenium import webdriver

def crawler():
    browser = webdriver.Chrome()
    browser.get('http://www.oromodictionary.com/articles/index.php?&page=1&ipp=All')
    h2 = browser.find_elements_by_tag_name("h2")
    news_list = []
    driver = webdriver.Chrome()
    url_set = set()
    for i in h2:
        url = i.find_element_by_tag_name('a').get_attribute('href')
        url_set.add(url)
    print(len(url_set))
    k = 0
    for url in url_set:
        print(url)
        driver.get(url)
        news_text = ''
        title = driver.find_element_by_tag_name('h1')
        news_text += title.text + "\n"
        try:
            p = driver.find_elements_by_tag_name('p')
            for pp in p:
                news_text += pp.text + '\n'
        except BaseException as e:
            print("该页无p")
        print(k)
        print(news_text)
        k += 1
        news_list.append(news_text)
    driver.close()
    browser.close()
    return news_list

