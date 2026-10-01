import os
from pathlib import Path
from playwright.sync_api import sync_playwright
import dotenv
dotenv.load_dotenv()

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
                                            "name": os.environ["cookie_name"],
                                            "value": token,
                                            "domain": os.environ["cookie_domain"],
                                            "path": os.environ["cookie_path"],
                                            "httpOnly": False,
                                            "secure": True,
                                        }
                                    ]
                                )
        self.page = self.context.new_page()
        self.page.goto(os.environ["bos_case_url"].format(caseNumber=case_number))

        print(
            f"Opened case: {case_number}"
        )

    def click_edit(self):

        self.page.get_by_role(
            "link",
            name="Validate"
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

    def validate_exception_granted(self) -> bool:
        self.page.wait_for_load_state("networkidle")
        locator = self.page.get_by_text("* Exception Granted on Case")
        return locator.is_visible()

    def capture_screenshot(self,incident_id: str,) -> str:
        base_dir = Path(__file__).resolve().parents[3]
        screenshot_dir = (base_dir/ "logs"/ "incidents"/ "screenshots")
        screenshot_dir.mkdir(
                        parents=True,
                        exist_ok=True,
        )
        screenshot_path = (
                            screenshot_dir
                            / f"{incident_id}.png"
                        )
        self.page.screenshot(
        path=str(screenshot_path),
        full_page=True,
        )
        return str(screenshot_path)

    def capture_url(self, incident_id: str,) -> str:
        current_url = self.page.url
        return current_url

    def capture_page_text(self,incident_id: str,) -> str:
        return self.page.locator(
            "body"
        ).inner_text()
    
    def get_visible_controls(self,incident_id: str,) -> str:
        controls = []

        # Buttons
        for el in self.page.get_by_role("button").all():
            try:
                controls.append({
                    "type": "button",
                    "text": el.inner_text().strip()
                })
            except Exception:
                pass

        # Links
        for el in self.page.get_by_role("link").all():
            try:
                controls.append({
                    "type": "link",
                    "text": el.inner_text().strip()
                })
            except Exception:
                pass

        # Checkboxes
        for el in self.page.get_by_role("checkbox").all():
            try:
                controls.append({
                    "type": "checkbox",
                    "text": el.get_attribute("aria-label")
                })
            except Exception:
                pass

        return controls
        

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()