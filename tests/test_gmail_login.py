import pytest
from config.constants import  USERNAME, PASSWORD,BAD_PASSWORD
from pages.gmail_inbox_page import GmailInboxPage
from pages.gmail_login_page import GmailLoginPage


@pytest.mark.smoke
def test_successful_gmail_login(page):
    login_page = GmailLoginPage(page)
    inbox_page = GmailInboxPage(page,USERNAME)
    login_page.navigate()
    login_page.enter_email(USERNAME)
    login_page.enter_password(PASSWORD)
    assert inbox_page.is_logged_in(), "Failed to log in to Gmail"

@pytest.mark.smoke
def test_is_failed_authentication(page):
    login_page = GmailLoginPage(page)
    login_page.navigate()
    login_page.enter_email(USERNAME)
    login_page.enter_password(BAD_PASSWORD)
    assert login_page.is_failed_authentication(), "Negative login to Gmail failed"


