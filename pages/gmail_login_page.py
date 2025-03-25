import pytest
from playwright.sync_api import Page, TimeoutError, expect
from config.constants import PAGE_LOAD_TIMEOUT, ACTION_TIMEOUT
from pages.gmail_inbox_page import GmailInboxPage
from utils.report import report


class GmailLoginPage:

    TITLE = "Gmail"
    BASE_URL = "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

    def __init__(self, page: Page):
        #Page elements locators
        self.page = page
        self.email_input = '#identifierId'
        self.next_button = 'button:has-text("Next")'
        self.password = 'div#password input[type="password"]'
        self.failure_label = ':text("Wrong password. Try again or click Forgot password to reset it.")'


    def navigate(self):
        try:
            report.log_info(f"Navigating to {GmailLoginPage.BASE_URL}")
            self.page.goto(GmailLoginPage.BASE_URL, timeout=PAGE_LOAD_TIMEOUT)
            report.log_info(f"Verify the TITLE is as expected - {GmailLoginPage.TITLE}")
            expect(self.page).to_have_title(GmailLoginPage.TITLE)
        except TimeoutError  as e:
            report.log_error(f"Timeout for loading page: {GmailLoginPage.BASE_URL}")
            raise e
        except Exception as e:
            report.log_error(self.page, f"Test failed: {e}")
            raise e



    def enter_email(self, email):
        try:
            report.log_info(f"Fill the user name field with: {email}")
            self.page.fill(self.email_input, email, timeout=ACTION_TIMEOUT)
            report.log_info(f"Click the next button")
            self.page.click(self.next_button, timeout=ACTION_TIMEOUT)
            report.log_info(f"Wait for password element to be visible")
            self.page.locator(self.password).wait_for(state='visible')
        except TimeoutError as e:
            report.log_error(f"Timeout error: {e}")
            raise e
        except AssertionError as e:
            report.log_error(f"Password is not visible: {e}")
        except Exception as e:
            report.log_error(f"Test failed: {e}")
            raise e

    def enter_password(self, password):
        try:
             report.log_info(f"Fill the password field with: {password}")
             self.page.fill(self.password, password, timeout=ACTION_TIMEOUT)
             report.log_info("Click the next button")
             self.page.click(self.next_button, timeout=ACTION_TIMEOUT)
        except TimeoutError as e:
            report.log_error(f"Timeout error: {e}")
            raise e
        except Exception as e:
            report.log_error(f"Test failed: {e}")
            raise e



    def is_failed_authentication(self):
        try:
            report.log_info(f"Verify the URL is is not the inbox URL")
            expect(self.page).not_to_have_url(GmailInboxPage.INBOX_URL)
            report.log_info(f"Verify the TITLE is as expected - {GmailLoginPage.TITLE}")
            expect(self.page).to_have_title(GmailLoginPage.TITLE)
            report.log_info("Verify failed login label is displayed")
            expect(self.page.locator(self.failure_label)).to_be_visible()
            return True
        except AssertionError as e:
            report.log_error(f"Authentication failure isn't displayed: {e}")
            return False
        except TimeoutError as e:
            report.log_error("Timeout for verifying login")
            return False
        except Exception as e:
            report.log_error(f"Test failed: {e}")
            return False



