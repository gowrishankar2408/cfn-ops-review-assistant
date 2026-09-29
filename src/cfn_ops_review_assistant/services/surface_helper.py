import os
from playwright.sync_api import sync_playwright


class SurfaceAdapter:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    import os
from pathlib import Path
from playwright.sync_api import sync_playwright


class SurfaceAdapter:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def launch_case(
        self,
        case_number: str,
        token: str,
    ):

        browser_path = os.getenv(
            "PLAYWRIGHT_BROWSER_PATH"
        )

        print(
            f"PLAYWRIGHT_BROWSER_PATH = {browser_path}"
        )

        if not browser_path:
            raise RuntimeError(
                "PLAYWRIGHT_BROWSER_PATH not configured."
            )

        if not Path(browser_path).exists():
            raise RuntimeError(
                f"Browser not found: {browser_path}"
            )

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            executable_path=browser_path,
            headless=False,
        )

        self.context = self.browser.new_context()
        self.context.add_cookies(
                                    [
                                        {
                                            "name": "CFNSession",
                                            "value": token,
                                            "domain": "home.commonwealth.com",
                                            "path": "/",
                                            "httpOnly": False,
                                            "secure": True,
                                        }
                                    ]
                                )
        self.page = self.context.new_page()
        self.page.goto(
            f"https://home.commonwealth.com/"
            f"Applications/BOS/support/cases/{case_number}"
        )

        print(
            f"Opened case: {case_number}"
        )

    def click_edit(self):

        self.page.get_by_role(
            "button",
            name="Edit"
        ).click()

    def select_exception_granted(self):

        self.page.get_by_label(
            "Exception Granted"
        ).check()

    def click_update_case(self):

        self.page.get_by_role(
            "button",
            name="Update Case"
        ).click()

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()