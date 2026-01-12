import pytest
from playwright.sync_api import expect
from config.settings import settings
from pages.dashboard_page import DashboardPage

@pytest.mark.smoke
class TestSmoke:
    def test_login_successful(self, login_page, dashboard_page):
        login_page.navigate()
        login_page.login(settings.USERNAME, settings.PASSWORD)
        assert dashboard_page.is_loaded()
        expect(dashboard_page.page).to_have_url(f"{settings.BASE_URL}/dashboard/index")

    def test_logout(self, page, login_page):
        # We manually login here to avoid invalidating the shared auth_state session
        login_page.navigate()
        login_page.login(settings.USERNAME, settings.PASSWORD)
        
        dashboard_page = DashboardPage(page)
        expect(dashboard_page.user_dropdown).to_be_visible()
        
        dashboard_page.logout()
        expect(login_page.login_button).to_be_visible()

    def test_primary_navigation_visible(self, auth_dashboard_page):
        auth_dashboard_page.navigate(f"{settings.BASE_URL}/dashboard/index")
        assert auth_dashboard_page.is_menu_item_visible("Admin")
        assert auth_dashboard_page.is_menu_item_visible("PIM")
        assert auth_dashboard_page.is_menu_item_visible("Leave")

    def test_app_health_check(self, auth_dashboard_page):
        auth_dashboard_page.navigate(f"{settings.BASE_URL}/dashboard/index")
        assert auth_dashboard_page.is_loaded()
        expect(auth_dashboard_page.page.get_by_role("alert")).not_to_be_visible()

    def test_basic_page_routing(self, auth_dashboard_page):
        auth_dashboard_page.navigate(f"{settings.BASE_URL}/dashboard/index")
        auth_dashboard_page.navigate_to_module("PIM")
        expect(auth_dashboard_page.page).to_have_url(f"{settings.BASE_URL}/pim/viewEmployeeList")
        expect(auth_dashboard_page.header_title).to_contain_text("PIM")
        
        auth_dashboard_page.navigate_to_module("Dashboard")
        expect(auth_dashboard_page.page).to_have_url(f"{settings.BASE_URL}/dashboard/index")
        expect(auth_dashboard_page.header_title).to_contain_text("Dashboard")
