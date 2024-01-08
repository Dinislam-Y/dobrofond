import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from into import starts_tests

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-cache')
# chrome_options.page_load_strategy = "normal" # дожидается загрузки всех ресурсов
chrome_options.page_load_strategy = "eager"  # дожидается загрузки DOM
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'https://admin.dobrofon.org/login'
driver.get(url)
time_costom = 0.5

# driver.refresh() перезагружает страницу
# driver.back() назад на страницу
# driver.forward() вперед на страницу

url_current = driver.current_url
print('Сайт', url_current)
time.sleep(time_costom)

title_current = driver.title
print('Заголовок:', title_current)
time.sleep(time_costom)

assert url == url_current, 'Ошибка в URL'
assert title_current == 'Авторизация', 'Некорректный заголовок'

username = driver.find_element('name', 'username')
username.click()
username.clear()
username.send_keys('n.test')
print(username.get_attribute('value'))
assert username.get_attribute('value') == 'n.test'
time.sleep(time_costom)

password = driver.find_element('name', 'password')
password.click()
password.clear()
password.send_keys('12345')
print(password.get_attribute('value'))
assert password.get_attribute('value') == '12345'
time.sleep(time_costom)

driver.find_element('xpath', "//button[@type='submit']").click()
# //button[@data-cy'123131' and @type='submit']
# //button[@type='submit']
# //button[text()='Вход']
time.sleep(time_costom)

driver.find_element('xpath', '//a[@href="/families"]').click()
time.sleep(time_costom)

driver.find_element('xpath', "//button[text()='Добавить семью']").click()
time.sleep(time_costom)

driver.find_element('xpath', "//button[text()='Сохранить']").click()
time.sleep(2)

