from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
# eleUserMessage = driver.find_element_by_id("user-message")


# eleUserMessage = driver.find_element_by_
eleUserMessage = driver.find_element(By.XPATH, '//*[@id="user-message"]')

eleUserMessage.clear()
eleUserMessage.send_keys("Test Python")

# //*[@id="user-message"]/label

showMessage = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
showMessage.click()


