from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "http://www.rahulshettyacademy.com/angularpractice/"

driver = webdriver.Chrome()


driver.get(url)


driver.maximize_window()

title = driver.title 

url = driver.current_url

print(title)
print(url)

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("John Cena")
driver.find_element(By.NAME, "email").send_keys("test")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click() 

message = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success" in message

time.sleep(2)




