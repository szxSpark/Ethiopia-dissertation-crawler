from selenium import webdriver
def crawler():
    browser = webdriver.Chrome()
    browser.get("http://www.oromoparliamentarians.org/")
    elements = browser.find_elements_by_class_name("MsoNormal")
    url_set = set()
    for e in elements:
        try:
            a = e.find_element_by_tag_name("a")
            url = a.get_attribute("href")
            if url != None:
                url_set.add(url)
        except Exception as e:
            pass
    print(len(url_set))
    news_list = []
    k = 0
    driver = webdriver.Chrome()
    for url in url_set:
        try:
            driver.get(url)
            k += 1
            print(k, url)
            news_text = ''
            try:
                elements = driver.find_elements_by_class_name("MsoNormal")
                for e in elements:
                    news_text += e.text+"\n"
            except BaseException as e:
                pass
            if len(news_text) > 10:
                news_list.append(news_text)
        except Exception as e:
            print("连接超时")

    print(len(news_list))
    driver.close()
    browser.close()
    return news_list

