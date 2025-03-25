from playwright.sync_api import Page, TimeoutError, expect
from utils.report import report
from config.constants import  USERNAME


class GmailInboxPage:
    INBOX_URL = "https://mail.google.com/mail/u/0/#inbox"

    def __init__(self, page: Page):
       self.page = page
       self.inbox_title = f"{USERNAME}@gmail.com"

    def is_logged_in(self):
        try:
            report.log_info(f"Verify the URL is as expected - {self.INBOX_URL}")
            expect(self.page).to_have_url(self.INBOX_URL)
            report.log_info(f"Verify the TITLE is as expected - {self.inbox_title}")
            expect(self.page).to_have_title(f'Inbox - {self.inbox_title} - Gmail')
            return True
        except AssertionError as e:
            report.log_error(f"Title is wrong, Expected: {self.inbox_title} ,Actual: {self.page.title()}")
            return False
        except TimeoutError as e:
            report.log_error("Timeout for verifying login")
            return False
        except Exception as e:
            report.log_error(f"Test failed: {e}")
            return False





