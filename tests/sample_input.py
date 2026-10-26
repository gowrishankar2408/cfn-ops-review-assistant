prompt = {
  "request_id": "DISC-85de1960-e87c-4d69-8fc5-c85a8ff0ad6a",
  "capability": "pps-custom-expiration",
  "version": "1.0",
  "incident_id": "INC-f13d60bd-548b-4d99-a593-d4bff105260d",
  "case_number": "24910726",
  "error": "Locator.click: Timeout 30000ms exceeded.\nCall log:\n  - waiting for get_by_role(\"button\", name=\"Update Notes\")\n",
  "screenshot": "C:\\Automations\\aws\\cfn-ops-review-assistant\\logs\\incidents\\screenshots\\24910726.png",
  "failed_step": {
    "action": "click",
    "target": {
      "role": "button",
      "name": "Update Notes"
    }
  },
  "capture_url": "https://home.commonwealth.com/Applications/BOS/support/cases/edit/24910726",
  "generated_at": "2026-10-07T09:52:33.142121",
  "artifact": {
    "name": "pps-custom-expiration",
    "version": "5.0",
    "inputs": {
      "case_number": "string"
    },
    "outputs": {
      "status": "string"
    },
    "steps": [
      {
        "action": "click",
        "target": {
          "role": "link",
          "name": "Edit"
        }
      },
      {
        "action": "check",
        "target": {
          "role": "checkbox",
          "name": "Exception Granted"
        }
      },
      {
        "action": "click",
        "target": {
          "role": "button",
          "name": "Update Notes"
        }
      }
    ],
    "checkpoint": {
      "text": "Exception Granted on Case"
    }
  },
  "visible_controls": [
    {
      "role": "button",
      "name": "Update Case"
    },
    {
      "role": "button",
      "name": "Cancel"
    }
  ]
}