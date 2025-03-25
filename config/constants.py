import os

# Browser type (chromium, firefox, webkit)
BROWSER_TYPE = os.getenv("BROWSER_TYPE", "chromium").lower()

# Timeouts in milliseconds
PAGE_LOAD_TIMEOUT = 10000   # 10 seconds
ACTION_TIMEOUT = 5000       # 5 seconds

# Test account details
USERNAME = os.getenv("GMAIL_USERNAME", "interviewautomation0")
PASSWORD = os.getenv("GMAIL_PASSWORD", "!Q2w3e$R")
BAD_PASSWORD = "pass_doesn't_exist"








