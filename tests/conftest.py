import pytest
from playwright.sync_api import Page, BrowserContext, Browser, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.base_page import BasePage
from config.settings import settings
import json
import os

@pytest.fixture(scope="session", autouse=True)
def configure_expect():
    expect.set_options(timeout=settings.TIMEOUT)

@pytest.fixture(scope="session")
def auth_state(browser: Browser):
    """
    Logs in once per session and saves the storage state.
    """
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(settings.USERNAME, settings.PASSWORD)
    
    # Wait for dashboard to ensure login success
    dashboard_page = DashboardPage(page)
    expect_loc = dashboard_page.user_dropdown
    expect_loc.wait_for()

    state = page.context.storage_state()
    page.close()
    return state

@pytest.fixture
def authenticated_page(browser: Browser, auth_state) -> Page:
    """
    Returns a page with the authentication state loaded.
    """
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def dashboard_page(page: Page):
    return DashboardPage(page)

@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def auth_dashboard_page(authenticated_page: Page):
    return DashboardPage(authenticated_page)
