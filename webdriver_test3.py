from selenium import webdriver 

driver = webdriver.chrome()
driver.get("https://www.google.com")

print driver.title
print driver.current_url

# driver.quit()
