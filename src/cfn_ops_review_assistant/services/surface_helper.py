import os
from pathlib import Path
from cfn_ops_review_assistant.utils.path_utils import get_project_root
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from cfn_ops_review_assistant.utils.path_utils import get_project_root
load_dotenv(get_project_root() / ".env")

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
        if not self.page:
            return None
        base_dir = get_project_root()
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
        if not self.page:
            return None
        current_url = self.page.url
        return current_url

    def capture_page_text(self,incident_id: str,) -> str:
        if not self.page:
            return None
        return self.page.locator(
            "body"
        ).inner_text()
    
    def get_visible_controls(self):

        controls = []

        ignored_controls = {
            "Case Manager",
            "Create Case",
            "Admin",
            "Echo Bot",
            "History",
            "Forms 0",
            "Files 1",
            "Commitments 0",
            "Child Cases 0",
            "Subcases 0",
            "You",
            "0",
            "testDocument.txt",
        }

        action_keywords = {
            "edit",
            "update",
            "save",
            "submit",
            "cancel",
            "open",
            "close",
            "validate",
            "approve",
            "reject",
            "reassign",
            "exception",
        }

        def should_include(name: str) -> bool:

            if not name:
                return False

            name = name.strip()

            if not name:
                return False

            if name in ignored_controls:
                return False

            if name.startswith("http"):
                return False

            if any(
                keyword in name.lower()
                for keyword in action_keywords
            ):
                return True

            return False

        # Buttons
        for el in self.page.get_by_role("button").all():
            try:

                name = el.inner_text().strip()

                if not should_include(name):
                    continue

                controls.append({
                    "role": "button",
                    "name": name
                })

            except Exception:
                pass

        # Links
        for el in self.page.get_by_role("link").all():
            try:

                name = el.inner_text().strip()

                if not should_include(name):
                    continue

                controls.append({
                    "role": "link",
                    "name": name
                })

            except Exception:
                pass

        # Checkboxes
        for el in self.page.get_by_role("checkbox").all():
            try:

                name = (
                    el.get_attribute("aria-label")
                    or ""
                ).strip()

                if not should_include(name):
                    continue

                controls.append({
                    "role": "checkbox",
                    "name": name
                })

            except Exception:
                pass

        # Remove duplicates
        unique_controls = []

        seen = set()

        for control in controls:

            key = (
                control["role"],
                control["name"]
            )

            if key in seen:
                continue

            seen.add(key)

            unique_controls.append(control)

        return unique_controls

    def execute_step(self,step: dict,):

        action = step["action"]

        target = step["target"]

        role = target["role"]

        name = target["name"]

        if action == "click":

            self.page.get_by_role(
                role,
                name=name
            ).click()

        elif action == "check":

            self.page.get_by_role(
                role,
                name=name
            ).check()

        else:

            raise RuntimeError(
                f"Unsupported action: {action}"
            )
        

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()