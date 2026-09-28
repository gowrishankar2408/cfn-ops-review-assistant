'''PSR Review Process'''
import os
import requests

from cfn_ops_review_assistant.processes.note_comparer import NoteComparer
from cfn_ops_review_assistant.models.summary_builder import SummaryBuilder

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
                    f"{marker} {edit_note.strip()}",
                )

        raise ValueError(
            "Unable to find ORIGINAL SUBMIT DATE and EDIT SUBMIT DATE notes."
        )

    def clean_note(self, note: str) -> str:
        lines = note.splitlines()
        filtered = []
        for line in lines:

            if line.startswith("ORIGINAL SUBMIT DATE:"):
                continue

            if line.startswith("EDIT SUBMIT DATE:"):
                continue

            filtered.append(line)

        return "\n".join(filtered)

class PSRReview:
    def __init__(self):
        self.host_name = os.getenv("hostName")
        self.entry_point = os.getenv("entryPoint")
        self.notes_url_template = os.getenv("notesUrl")
        self.clientID = os.getenv("clientid")
        self.clientSecret = os.getenv("clientsecret")

    def get_case_notes(self, case_number: str, token: str):

        '''Fetch case notes for a given case number using the provided token.'''

        if not case_number or not token:
            raise ValueError("Both case_number and token are required.")
        notesURL = self.host_name + self.entry_point + self.notes_url_template.format(caseNumber=case_number)
        response = requests.get(notesURL, headers={"client_id": self.clientID, "client_secret": self.clientSecret })
        return (response.content)

def review(case_number, token):
    process = PSRReview()
    note_processor = NoteParser()
    case_notes = process.get_case_notes(case_number, token)
    parsed_notes = note_processor.extract_notes(case_notes)
    original_note = note_processor.clean_note(parsed_notes[0])
    edit_note =  note_processor.clean_note(parsed_notes[1])
    print("-" * 50)
    print((original_note))
    print("-" * 50)
    print((edit_note))
    comparison_result =NoteComparer().compare(original_note, edit_note)
    summary = SummaryBuilder().build(
        case_number,
        comparison_result,
    )
    print("-" * 50)
    return {
            "summary": summary,
            "comparison_result": comparison_result,
            }
    