import os
from random import randint, choice
from string import ascii_letters
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from locators import basic_locators
from pages.base_page import BasePage


class DashboardPageException(Exception):
    ...


class LoginPage(BasePage):

    def log_in(self, login: str, password: str):
        """ Метод входа входа в аккаунт """
        try:
            self.click_element(self.find(self.locators.LOGIN_LOCATOR))
            element_login_input = self.find(self.locators.INPUT_LOGIN)
            element_login_input.send_keys(login)
            element_password_input = self.find(self.locators.INPUT_PASSWORD)
            element_password_input.send_keys(password)
            element_password_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            return False

        return DashboardPage(driver=self.driver)


class DashboardPage(BasePage):

    locators_create_campaign = basic_locators.CampaignNewLocators()
    url = "https://target-sandbox.my.com/dashboard"

    @allure.step("Step 2 - method create new campaign")
    def create_new_campaign(self, name: str):
        try:
            self.find(self.locators_create_campaign.CREATE_NEW_CAMPAIGN).click()

            product_vk = self.find(self.locators_create_campaign.PRODUCT_VK)
            product_vk.click()

            input_link = self.find(self.locators_create_campaign.INPUT_PLACEHOLDER_LINK)
            input_link.send_keys("https://genius.com")

            tizer_button = self.find(self.locators_create_campaign.TIZER)
            tizer_button.click()

            name_campaign = self.find(self.locators_create_campaign.INPUT_NAME_CAMPAIGN)
            name_campaign.clear()
            name_campaign.send_keys(name)

            header_ad = self.find(self.locators_create_campaign.INPUT_PLACEHOLDER_HEADER)
            header_ad.send_keys(self.random_str())

            text_ad = self.find(self.locators_create_campaign.INPUT_AD)
            text_ad.send_keys(self.random_str())

            load_pictures_button = self.driver.find_element(*self.locators_create_campaign.LOAD_PICTURES)
            load_pictures_button.send_keys(os.getcwd()+"/files/p.png")

            self.find(self.locators_create_campaign.SAVE_BUTTON_PIC).click()
            self.find(self.locators_create_campaign.SUBMIT_BANNER_BUTTON).click()

        except DashboardPageException as ex:
            return ex

        return True


