import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    PAGE_URL = Links.LOGIN

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    LOGIN_ERROR = ("xpath", "//div[text()='Невозможно войти с предоставленными учетными данными.']")
    USERNAME_FIELD_REQUIRED = ("xpath", "//div[text()='Поле обязательно для заполнения']")

    def into_login(self, login, password):
        self.open()
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit_button()

    def login_error(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_ERROR))

    @allure.step("Пишу логин")
    def enter_login(self, login):
        enter_login = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        enter_login.clear()
        assert enter_login.get_attribute("value") == "", "В поле находится текст"
        enter_login.send_keys(login)

    @allure.step("Пишу пароль")
    def enter_password(self, password):
        enter_password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        enter_password.clear()
        assert enter_password.get_attribute("value") == "", "В поле находится текст"
        enter_password.send_keys(password)

    @allure.step("Нажал на 'Войти'")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
