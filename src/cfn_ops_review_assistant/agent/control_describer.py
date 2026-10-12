KNOWN_CONTROLS = {
    "Workflow": {
        "description": (
            "Case workflow operations such as "
            "Accept, Assign, Change Status, "
            "Close, Dispatch and Run Task Set"
        ),
        "children": [
            "Accept",
            "Assign",
            "Change Status",
            "Close",
            "Dispatch",
            "Run Task Set",
        ],
    },

    "Logs": {
        "description":
            "View case history and activity logs",
        "children": ["Commitment",
                     "Email",
                     "Notes",
                     "Research"],
    },

    "Actions": {
        "description":
            "Additional case actions and utilities",
        "children": [],
    },

    "Edit": {
        "description":
            "Open case in edit mode to modify values",
        "children": [],
    },

    "Close": {
        "description":
            "Close the current case",
        "children": [],
    }
}