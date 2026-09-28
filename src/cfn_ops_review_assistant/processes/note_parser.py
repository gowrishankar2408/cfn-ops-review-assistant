'''Class to parse the notes extracted from the CRM API'''

import json

class NoteParser:

    def extract_notes(
        self,
        raw_notes: dict,
    ) -> tuple[str, str]:
        # Convert raw_notes to a dictionary if it's in bytes or string format
        if isinstance(raw_notes, bytes):
            raw_notes = json.loads(raw_notes.decode("utf-8"))
        elif isinstance(raw_notes, str):
            raw_notes = json.loads(raw_notes)

        parsed_notes = raw_notes.get("data", [])

        marker = "EDIT SUBMIT DATE:"

        for each_note in parsed_notes:
            note = each_note.get("note", "")

            if (
                "ORIGINAL SUBMIT DATE" in note
                and marker in note
            ):
                original_note, edit_note = note.split(
                    marker,
                    1,
                )

                return (
                    original_note.strip(),
                    edit_note.strip()
                )

        raise ValueError(
            "Unable to find ORIGINAL SUBMIT DATE and EDIT SUBMIT DATE notes."
        )