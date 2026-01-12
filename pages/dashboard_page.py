from playwright.sync_api import Page
from pages.base_page import BasePage
from config.settings import settings

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.user_dropdown = self.page.locator(".oxd-userdropdown-tab")
        self.logout_link = self.page.get_by_role("menuitem", name="Logout")
        self.header_title = self.page.locator(".oxd-topbar-header-title")
        self.time_at_work_widget = self.page.get_by_text("Time at Work")
        self.side_menu = self.page.locator(".oxd-sidepanel-body")

    def is_loaded(self):
        try:
            self.user_dropdown.wait_for(state="visible", timeout=settings.TIMEOUT)
            return True
        except:
            return False


    def logout(self):
        self.user_dropdown.click()
        self.logout_link.click()

    def get_header_title(self):
        self.header_title.wait_for()
        return self.header_title.text_content()

    def navigate_to_module(self, module_name: str):
        self.page.get_by_role("link", name=module_name).click()

    def is_menu_item_visible(self, module_name: str) -> bool:
        self.side_menu.wait_for(state="visible")
        return self.page.get_by_role("link", name=module_name).is_visible()

