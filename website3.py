from selenium import webdriver

def crawler():
    browser = webdriver.Chrome()
    browser.get('http://www.gubirmans.com/')
    p = browser.find_elements_by_tag_name("p")
    news_list = []
    print(len(p))
    k = 0
    news_text = ''
    for i in p:
        try:
            if i.get_attribute('class') == None or i.get_attribute('class') == '':
                print(k)
                k += 1
                if len(i.text) > 7:
                    news_text += i.text + '\n'
                # print(news_text)
        except BaseException as e:
            print("该页无p")
    news_list.append(news_text)

    browser.close()
    return news_list

crawler()

