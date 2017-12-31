from selenium import webdriver

def crawler():
    website = ['http://www.oromummaa.com/index.php?option=com_content&view=article&id=48:oromumaa-wtuoga&catid=4:home-news-english&Itemid=20',
               'http://www.oromummaa.com/index.php?option=com_content&view=article&id=43:ethiopia-using-aid-as-weapon-of-oppression-&catid=4:home-news-english&Itemid=20']
    url_set = set()
    browser = webdriver.Chrome()
    news_list = []
    k = 0
    for wb in website:
        browser.get(wb)
        news_text = ''
        try:
            p = browser.find_elements_by_tag_name('p')
            for pp in p:
                if pp.get_attribute('class') == None or pp.get_attribute('class') == '':
                    news_text += pp.text + '\n'
        except BaseException as e:
            print("该页无p")
        news_list.append(news_text)

    print(len(news_list))
    browser.close()
    return news_list
