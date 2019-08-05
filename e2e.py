from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://rakesh635:321661be-ee97-4df8-97c3-c05a48f84e54@ondemand.eu-central-1.saucelabs.com')
