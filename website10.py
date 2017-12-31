from selenium import webdriver
def crawler():
    browser = webdriver.Chrome()

    # 新闻共216页
    url_base = "https://kichuu.com/category/news/africa/page/"
    url_number = 0
    url = ""
    # 每个新闻列表页面，共216个
    url_set = set()
    for i in range(216):
        try:
            url_number = i+1
            url = url_base + str(url_number) +"/"
            browser.get(url)
            # 每个新闻列表涵盖10条新闻
            read_more = browser.find_elements_by_class_name("mh-excerpt-more")
            print(len(url_set))
            for i in read_more:
                urll = i.get_attribute("href")
                if urll != None:
                    url_set.add(urll)
        except Exception as e:
            print("连接超时")

    driver = webdriver.Chrome()
    news_list = []
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
    driver.close()
    browser.close()
    return news_list