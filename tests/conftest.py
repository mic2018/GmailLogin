import pytest
from playwright.sync_api import sync_playwright
from config.constants import BROWSER_TYPE, PAGE_LOAD_TIMEOUT, ACTION_TIMEOUT
from utils.report import report

@pytest.fixture(scope="function")
def page(request):
    browser_type = request.config.getoption("--browser") or BROWSER_TYPE
    report.log_info(f"Setting up browser: {browser_type}")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--start-maximized',
                '--window-size=1280,720' # Start maximized
            ]
        )

        # Create a new browser context
        context = browser.new_context()
        context.set_default_navigation_timeout(PAGE_LOAD_TIMEOUT)
        context.set_default_timeout(ACTION_TIMEOUT)
        page = context.new_page()


        try:
            yield page
        except Exception as e:
            report.log_error(f"Error during browser session: {e}")
            report.attach_screenshot(page, "browser_failure")
            raise
        finally:
            report.log_info("Closing browser")
            browser.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser type: chromium, firefox, webkit"
    )
