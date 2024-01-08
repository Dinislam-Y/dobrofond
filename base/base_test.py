import pytest
from config.data import Data
from pages.families_page import FamiliesPage
from pages.families_page import AddFamily
from pages.login_page import LoginPage



class BaseTest:
    data: Data

    login_page: LoginPage
    families_page: FamiliesPage
    add_family: AddFamily

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.families_page = FamiliesPage(driver)
        request.cls.add_family = AddFamily(driver)
