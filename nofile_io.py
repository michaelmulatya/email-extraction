from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://nofile.io/f/K118x0bNS9a/Beano+%26ndash%3B+2+February+2019.pdf')
try:
    download = driver.find_element_by_class_name('downloadButton')
    download.click()
except:

    print('https://nofile.io/f/K118x0bNS9a/Beano+%26ndash%3B+2+February+2019.pdf')