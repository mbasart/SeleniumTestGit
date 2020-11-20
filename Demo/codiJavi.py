from selenium import webdriver
import time

FirefoxDriver = './drivers/geckodriver.exe'
ChromeDriver = './drivers/chromedriver.exe'

#driver = webdriver.Firefox(executable_path=FirefoxDriver)
driver = webdriver.Chrome(r"C:\Users\mbd27\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://www.google.com/")

driver.switch_to.frame(driver.find_element_by_xpath('//div[@id = "cnsw"]//iframe'))
driver.find_element_by_xpath('//span[text()="Acepto"]').click()
time.sleep(3)

driver.close()