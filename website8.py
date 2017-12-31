from selenium import webdriver

def crawler():
    browser = webdriver.Chrome()
    browser.get("https://qeerroo.org/")
    more_link = browser.find_elements_by_class_name("more-link")
    url_set = set()
    for link in more_link:
        url_set.add(link.get_attribute("href"))
    news_list = []
    k = 0
    driver = webdriver.Chrome()
    for url in url_set:
        driver.get(url)
        news_text = ''
        try:
            p = driver.find_elements_by_tag_name('p')
            for pp in p:
                news_text += pp.text + '\n'
        except BaseException as e:
            print("该页无p")
        news_list.append(news_text)

    print(len(news_list))
    driver.close()
    browser.close()
    return news_list
