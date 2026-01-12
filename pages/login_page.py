from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from config.settings import settings

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.error_alert = self.page.get_by_role("alert")
        self.required_error = self.page.get_by_text("Required")

    def navigate(self):
        super().navigate(settings.BASE_URL)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_alert.text_content()

    def is_login_button_visible(self):
        return self.login_button.is_visible()
