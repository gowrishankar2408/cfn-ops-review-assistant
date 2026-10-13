from cfn_ops_review_assistant.services.surface_helper import SurfaceAdapter
from dotenv import load_dotenv
from cfn_ops_review_assistant.utils.path_utils import get_project_root
load_dotenv(get_project_root() / ".env")

adapter = SurfaceAdapter()

try:

    adapter.launch_case(
        case_number="28929696",
        token="dummy-token",
    )

    input(
        "\nPress Enter to close browser..."
    )

finally:

    adapter.close()