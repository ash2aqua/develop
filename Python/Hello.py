from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window
driver.get("https://www.google.com/")
print("Application Title is", driver.title)
print("Application URK=L is, ", driver.current_url)
driver.quit()
driver