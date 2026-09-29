from cfn_ops_review_assistant.services.surface_helper import SurfaceAdapter
import dotenv
dotenv.load_dotenv()

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