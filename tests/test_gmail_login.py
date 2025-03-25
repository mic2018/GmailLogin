import pytest
from config.constants import  USERNAME, PASSWORD,BAD_PASSWORD
from pages.gmail_inbox_page import GmailInboxPage
from pages.gmail_login_page import GmailLoginPage


@pytest.mark.smoke
def test_successful_gmail_login(page):
    should_succeed = True
    login_page = GmailLoginPage(page)

    login_page.navigate()
    login_page.enter_email(USERNAME)
    assert login_page.enter_password(PASSWORD, should_succeed) , "Failed to log in to Gmail"


@pytest.mark.smoke
def test_is_failed_authentication(page):
    should_succeed = False
    login_page = GmailLoginPage(page)
    login_page.navigate()
    login_page.enter_email(USERNAME)
    assert login_page.enter_password(BAD_PASSWORD, should_succeed), "Negative login to Gmail failed"



