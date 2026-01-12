from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def get_by_role(self, role: str, **kwargs) -> Locator:
        return self.page.get_by_role(role, **kwargs)

    def get_by_text(self, text: str, **kwargs) -> Locator:
        return self.page.get_by_text(text, **kwargs)
    
    def get_by_label(self, label: str, **kwargs) -> Locator:
        return self.page.get_by_label(label, **kwargs)
    
    def get_by_placeholder(self, placeholder: str, **kwargs) -> Locator:
        return self.page.get_by_placeholder(placeholder, **kwargs)

    def wait_for_url(self, url: str):
        self.page.wait_for_url(url)
