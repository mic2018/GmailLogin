import logging
import os
import allure
import pytest
from playwright.sync_api import Page

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/test.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

class Report:
    def __init__(self):
        self.logger = logging.getLogger()

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)
        pytest.fail(f"Test failed due to: {message}")

report = Report()
