from selenium import webdriver
import re





browser = webdriver.Chrome()
starturl = 'https://www.forexlasers.com/forums/'
browser.get(starturl)
domain = 'forexlasers.com'
domregex = re.compile(r'{0}'.format(domain))
# login = browser.find_element_by_xpath('.//span[@class="member-nav__login-text"]')
# login.click()
# user=browser.find_element_by_xpath('.//input[contains(@name,"vb_login_username")]')
# user.send_keys('tforexx')
# pasw = browser.find_element_by_xpath('.//input[contains(@name,"vb_login_password")]')
# pasw.send_keys('ftrader341678')
#
# browser.find_element_by_xpath('.//input[contains(@value,"Login")]').click()

all_url = []
def getlink():
    links = []
    urls = browser.find_elements_by_xpath('//a')
    for link in urls:
        dom = link.get_attribute('href')
        try:
            ex = re.search(r'forexlasers.com',dom)
            if ex:

                if dom not in all_url:
                    links.append(dom)
                    print (links)
        except:
            print('skipped')
        all_url.extend(links)



res = []
def getmails(link):
    browser.get(link)
    response = browser.page_source
    emails = re.findall(r'[\w\.-]+@[\w\.-]+',response)
    for email in emails:
        print (email)
        if email not in res:
            res.append(email)
    print(res)
#[\w\.-]+@[\w\.-]+
checked = [starturl]
getlink()
for lead in all_url:
    if lead not in checked:
        getmails(lead)
        getlink()
        checked.append(lead)

        #//*[@id="ui-inner"]/header[1]/div/ul[2]/li[2]/span/form/input[5]