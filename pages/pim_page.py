from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from config.settings import settings

class PIMPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = self.page.get_by_role("button", name="Add") 
        self.first_name_input = self.page.get_by_placeholder("First Name")
        self.last_name_input = self.page.get_by_placeholder("Last Name")
        # Structure often: .oxd-input-group > label(Employee Id) ... input
        # Using a slightly robust xpath or css if get_by_label fails, but let's try get_by_label approach first or locate by structure
        # self.employee_id_input = self.page.get_by_label("Employee Id") # This often fails in OHRM because label for attr is missing
        self.employee_id_input = self.page.locator(".oxd-input-group:has-text('Employee Id') input")
        
        self.save_button = self.page.get_by_role("button", name="Save")
        self.success_message = self.page.get_by_text("Successfully Saved") # Toast message
        # Personal Details header might be h6 or just text
        self.personal_details_header = self.page.locator("h6").filter(has_text="Personal Details") 


    def click_add_employee(self):
        self.add_button.click()

    def fill_employee_details(self, first_name, last_name, emp_id=None):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        if emp_id:
            self.employee_id_input.fill(emp_id)

    def save(self):
        self.save_button.click()
    
    def is_success_message_visible(self):
        try:
            self.success_message.wait_for(timeout=settings.TIMEOUT)
            return True
        except:
            return False
