import pytest
from playwright.sync_api import expect
from config.settings import settings
from pages.pim_page import PIMPage
from utils.data_factory import DataFactory

@pytest.mark.pim
@pytest.mark.regression
class TestPIM:
    @pytest.fixture
    def pim_page(self, auth_dashboard_page):
        auth_dashboard_page.navigate(settings.BASE_URL) # Go to base url (login check will pass due to cookies)
        auth_dashboard_page.navigate_to_module("PIM")
        return PIMPage(auth_dashboard_page.page)

    def test_add_employee_happy_path(self, pim_page):
        pim_page.click_add_employee()
        
        # Data Generation
        first_name = DataFactory.get_unique_name("Test")
        last_name = "User"
        emp_id = DataFactory.get_unique_id()
        
        pim_page.fill_employee_details(first_name, last_name, emp_id)
        pim_page.save()
        
        # Assertions
        assert pim_page.is_success_message_visible(), "Success toast did not appear"
        expect(pim_page.personal_details_header).to_be_visible()
        
        # Verify default values or just that we are on the page
        expect(pim_page.page.get_by_placeholder("First Name")).to_have_value(first_name)
