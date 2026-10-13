import os
import urllib3

from cfn_ops_review_assistant.llm.copilot_provider import (
    CopilotProvider,
)
urllib3.disable_warnings()
provider = CopilotProvider(
    os.getenv(
        "copilot_secret"
    )
)

response = provider.generate(
    """
Current Capability Artifact

{
  "name": "pps-custom-expiration"
}

Failed Step

{
  "action": "click",
  "target": {
    "role": "link",
    "name": "Validate"
  }
}

Visible Controls

[
  {
    "role": "link",
    "name": "Edit"
  }
]

Current URL

https://example.com

Failure

Locator.click timeout
"""
)

print(response)