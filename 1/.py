from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ссылка на страницу с багом (для проверки, что тест падает)
# link = "http://suninjuly.github.io/registration2.html"
# Ссылка на рабочую страницу (для проверки, что тест проходит)
link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля (селекторы нужно подобрать самостоятельно)
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']") # Пример
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']") # Пример
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']") # Пример
    input3.send_keys("test@example.com")

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем загрузки и проверяем результат
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
