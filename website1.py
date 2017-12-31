from selenium import webdriver

def crawler():
    browser = webdriver.Chrome()
    browser.get('https://www.bbc.com/afaanoromoo')
    '''
    website = https://www.bbc.com/afaanoromoo
    class: title-link
    class="links-list__link" 
    class = story-body__introduction
    tag = p
    '''
    title_link = browser.find_elements_by_class_name("title-link")
    links_list_link = browser.find_elements_by_class_name("links-list__link")
    title_link.extend(links_list_link)
    news_list = []
    driver = webdriver.Chrome()
    for i in title_link:
        news_text = ''
        try:
            url = i.get_attribute('href')
            print(url)
            driver.get(url)
        except BaseException as e:
            print(e)
        try:
            intro = driver.find_element_by_class_name("story-body__introduction").text
            news_text += intro+'\n'
        except BaseException as e:
            print("该页intro")
        try:
            p = driver.find_elements_by_tag_name('p')
            for pp in p:
                if pp.get_attribute('class') == None or  pp.get_attribute('class') == '':
                    news_text += pp.text + '\n'
        except BaseException as e:
            print("该页无p")
        news_list.append(news_text)
    driver.close()
    browser.close()
    return news_list

