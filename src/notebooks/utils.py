def load_page(url):
    #, executable_path=rutaLocal+r'\build\geckodriver.exe'
    driver = webdriver.Firefox(firefox_options=options,firefox_profile=profile, firefox_binary=binary, executable_path='geckodriver.exe')
    #driver.implicitly_wait(120)
    driver.get(url)
    return driver