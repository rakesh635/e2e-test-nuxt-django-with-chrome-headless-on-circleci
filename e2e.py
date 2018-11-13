from selenium import webdriver


remote = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=webdriver.DesiredCapabilities.CHROME
)

remote.get_page('http://127.0.0.1:8000')
