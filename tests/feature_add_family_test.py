import time

import allure
import pytest

from base.base_test import BaseTest


@allure.feature("Profile Functionality")
class TestFeatureAddFamily(BaseTest):

    @allure.title("Login")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_login_xerror(self):
        self.login_page.into_login('12345', '12345')
        self.login_page.login_error()

    @allure.title("Create person")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_person(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.last_name('Маск')
        self.add_family.first_name('Илон')
        self.add_family.patronymic('Рив')
        self.add_family.birth_date('28061971')
        self.add_family.choice_date()
        time.sleep(0.5)
        self.add_family.persons_gender_icon()
        self.add_family.men_gender()
        self.add_family.phone_number('9281112233')
        self.add_family.dadata_meta('г Москва, ул 13-я Парковая, д 11')
        time.sleep(0.5)
        self.add_family.choice_address()
        self.add_family.address_comment('Недавно переехал в Махачкалу')
        time.sleep(1)
        self.add_family.save_family()
        time.sleep(1)
        try:
            self.driver.switch_to.alert.accept()
        except:
            print("alert не вызвался")
        time.sleep(0.5)
        self.add_family.is_created('Недавно переехал в Махачкалу')
        time.sleep(0.5)


@allure.feature("Validation check")
class TestValidationCheck(BaseTest):

    @allure.title("Firstname check")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_validation_check_firstname(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.last_name('Маск')
        self.add_family.patronymic('Рив')
        self.add_family.birth_date('28061971')
        self.add_family.choice_date()
        time.sleep(0.5)
        self.add_family.persons_gender_icon()
        self.add_family.men_gender()
        self.add_family.phone_number('9281112233')
        self.add_family.dadata_meta('г Москва, ул 13-я Парковая, д 11')
        time.sleep(0.5)
        self.add_family.choice_address()
        self.add_family.address_comment('Недавно переехал в Махачкалу')
        time.sleep(1)
        self.add_family.save_family()
        time.sleep(1)
        self.add_family.validation_check()

    @allure.title("Lastname check")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_validation_check_lastname(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.first_name('Илон')
        self.add_family.patronymic('Рив')
        self.add_family.birth_date('28061971')
        self.add_family.choice_date()
        time.sleep(0.5)
        self.add_family.persons_gender_icon()
        self.add_family.men_gender()
        self.add_family.phone_number('9281112233')
        self.add_family.dadata_meta('г Москва, ул 13-я Парковая, д 11')
        time.sleep(0.5)
        self.add_family.choice_address()
        self.add_family.address_comment('Недавно переехал в Махачкалу')
        time.sleep(1)
        self.add_family.save_family()
        self.add_family.validation_check()
        time.sleep(1)

    @allure.title("Address check")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_validation_check_address(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.last_name('Маск')
        self.add_family.first_name('Илон')
        self.add_family.birth_date('28061971')
        self.add_family.choice_date()
        time.sleep(0.5)
        self.add_family.persons_gender_icon()
        self.add_family.men_gender()
        self.add_family.phone_number('9281112233')
        time.sleep(0.5)
        self.add_family.save_family()
        self.add_family.test_validation_check_address()

    @allure.title("Phone check")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_validation_check_phone(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.last_name('Маск')
        self.add_family.first_name('Илон')
        self.add_family.birth_date('28061971')
        self.add_family.choice_date()
        time.sleep(0.5)
        self.add_family.persons_gender_icon()
        self.add_family.men_gender()
        time.sleep(0.5)
        self.add_family.dadata_meta('г Москва, ул 13-я Парковая, д 11')
        time.sleep(0.5)
        self.add_family.choice_address()
        self.add_family.save_family()
        time.sleep(2)
        self.add_family.test_validation_check_phone()

    @allure.title("Birthdate check")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_validation_check_birth_date(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.last_name('Маск')
        self.add_family.first_name('Илон')
        self.add_family.phone_number('9281112233')
        self.add_family.persons_gender_icon()
        self.add_family.men_gender()
        time.sleep(0.5)
        self.add_family.dadata_meta('г Москва, ул 13-я Парковая, д 11')
        time.sleep(0.5)
        self.add_family.choice_address()
        self.add_family.save_family()
        time.sleep(1)
        self.add_family.validation_check()

    @allure.title("Gender check")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_validation_check_birth_gender(self):
        self.login_page.into_login(self.data.LOGIN, self.data.PASSWORD)
        self.families_page.families_button()
        self.families_page.add_family()
        self.add_family.last_name('Маск')
        self.add_family.first_name('Илон')
        self.add_family.patronymic('Рив')
        self.add_family.birth_date('28061971')
        self.add_family.phone_number('9281112233')
        self.add_family.choice_date()
        time.sleep(0.5)
        self.add_family.dadata_meta('г Москва, ул 13-я Парковая, д 11')
        time.sleep(0.5)
        self.add_family.choice_address()
        self.add_family.save_family()
        time.sleep(1)
        self.add_family.validation_check()
