import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class FamiliesPage(BasePage):
    PAGE_URL = Links.FAMILIES

    FAMILIES_BUTTON = ("xpath", "//a[@href='/families']")
    ADD_FAMILY = ("xpath", "//button[text()='Добавить семью']")

    @allure.step("Клип иконке 'Семьи'")
    def families_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FAMILIES_BUTTON)).click()

    def add_family(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_FAMILY)).click()


class AddFamily(BasePage):
    PAGE_URL = Links.FAMILIES

    SAVE_FAMILY = ("xpath", "//button[text()='Сохранить']")

    LASTNAME = ("xpath", "//input[@name='last_name']")
    FIRSTNAME = ("xpath", "//input[@name='first_name']")
    PATRONYMIC = ("xpath", "//input[@name='patronymic']")
    BIRTH_DATE = ("xpath", "//input[@name='birth_date']")
    PERSONS_GENDER = ("xpath", "//div[@class=' css-1xc3v61-indicatorContainer']")
    PHONE_NUMBER = ("xpath", "//input[@name='phone_number']")
    DADATA_META = ("xpath", "//input[@name='dadata_meta']")
    ADDRESS_COMMENT = ("xpath", "//textarea[@name='address_comment']")
    CLOSE_WINDOW = ("xpath", "//button[@class='close-btn']")
    YES_DELETE = ("xpath", "//button[text()='Да, удалить']")
    NO_DELETE = ("xpath", "//button[text()='Нет']")
    MEN_GENDER = ("xpath", "//div[@class=' css-5bqg3t-option']")
    FEMALE_GENDER = ("xpath", "//div[@class=' css-npcpkn-option']")
    CHOICE_DATE = ("xpath", "//div[@class='react-datepicker__day react-datepicker__day--028 "
                            "react-datepicker__day--selected']")
    CHOICE_ADDRESS = ("xpath", "//button[@class='react-dadata__suggestion'][1]")
    USER = ("xpath", "//h1[@class='Heading_heading__dB_bW Heading_h1__MIh7C undefined']")
    DESCRIPTION_ADDRESS_COMMENT = ("xpath", "//div[@class='Descriptions_value__NEoDZ']")
    EDIT = ("xpath", "//button[@class='Button_button__q6YWL Button_white__Q222p Button_large__nmqYG pl-14']")
    REQUIRED_FIELD = ("xpath", "//div[text()='Поле обязательно для заполнения']")
    REQUIRED_FIELD_ADDRESS = (
        "xpath", "//div[text()='Укажите город или населенный пункт, Укажите улицу, Укажите номер дома']")
    REQUIRED_FIELD_PHONE = ("xpath", "//div[text()='Некорректный номер телефона.']")

    def __init__(self, driver):
        super().__init__(driver)
        self.XPATH = None

    def save_family(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_FAMILY)).click()

    def last_name(self, new_last_name):
        last_name = self.wait.until(EC.element_to_be_clickable(self.LASTNAME))
        last_name.clear()
        assert last_name.get_attribute("value") == "", "В поле находится текст"
        last_name.send_keys(new_last_name)

    def input_clear(self, XPATH):
        self.wait.until(EC.element_to_be_clickable(XPATH)).clear()

    def first_name(self, new_first_name):
        first_name = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME))
        first_name.clear()
        assert first_name.get_attribute("value") == "", "В поле находится текст"
        first_name.send_keys(new_first_name)
        self.first_name = new_first_name

    def patronymic(self, new_patronymic):
        patronymic = self.wait.until(EC.element_to_be_clickable(self.PATRONYMIC))
        patronymic.clear()
        assert patronymic.get_attribute("value") == "", "В поле находится текст"
        patronymic.send_keys(new_patronymic)

    def birth_date(self, new_birth_date):
        birth_date = self.wait.until(EC.element_to_be_clickable(self.BIRTH_DATE))
        birth_date.clear()
        birth_date.send_keys(new_birth_date)

    def phone_number(self, new_phone_number):
        phone_number = self.wait.until(EC.element_to_be_clickable(self.PHONE_NUMBER))
        phone_number.clear()
        phone_number.send_keys(new_phone_number)

    def dadata_meta(self, new_dadata_meta):
        dadata_meta = self.wait.until(EC.element_to_be_clickable(self.DADATA_META))
        dadata_meta.clear()
        dadata_meta.send_keys(new_dadata_meta)

    def address_comment(self, new_address_comment):
        address_comment = self.wait.until(EC.element_to_be_clickable(self.ADDRESS_COMMENT))
        address_comment.clear()
        address_comment.send_keys(new_address_comment)

    def close_window(self):
        self.wait.until(EC.element_to_be_clickable(self.CLOSE_WINDOW)).click()

    def yes_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.YES_DELETE)).click()

    def no_delete(self):
        self.wait.until(EC.element_to_be_clickable(self.NO_DELETE)).click()

    def is_created(self, new_address_comment):
        self.wait.until(EC.invisibility_of_element_located(self.SAVE_FAMILY))
        self.wait.until(EC.visibility_of_element_located(self.USER))
        self.wait.until(EC.element_to_be_clickable(self.EDIT)).click()
        self.wait.until(EC.text_to_be_present_in_element_value(self.ADDRESS_COMMENT, new_address_comment))

    def validation_check(self):
        self.wait.until(EC.visibility_of_element_located(self.REQUIRED_FIELD))

    def test_validation_check_address(self):
        self.wait.until(EC.visibility_of_element_located(self.REQUIRED_FIELD_ADDRESS))

    def test_validation_check_phone(self):
        self.wait.until(EC.visibility_of_element_located(self.REQUIRED_FIELD_PHONE))

    def men_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.MEN_GENDER)).click()

    def female_gender(self):
        self.wait.until(EC.element_to_be_clickable(self.FEMALE_GENDER)).click()

    def persons_gender_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.PERSONS_GENDER)).click()

    def choice_date(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOICE_DATE)).click()

    def choice_address(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOICE_ADDRESS)).click()
