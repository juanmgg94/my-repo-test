from selenium import webdriver
import time


driver = webdriver.Chrome()


driver.get("https://www.google.com")


driver.maximize_window()

title = driver.title 

url = driver.current_url

print(title)
print(url)

time.sleep(2)


