from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def test_func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    button = browser.find_element(By.ID, "book").click()

    num = browser.find_element(By.ID, "input_value").text
    result = test_func(num)

    answer = browser.find_element(By.ID, "answer").send_keys(result)

    subbmit = browser.find_element(By.ID, "solve").click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text+"это сообщение из уведомления, которое нужно отправить в ответ")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()