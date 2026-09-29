'''PSR Review Process'''
import os
import requests

from cfn_ops_review_assistant.services.note_comparer import NoteComparer
from cfn_ops_review_assistant.models.models import ReviewResult
from cfn_ops_review_assistant.models.summary_builder import SummaryBuilder
from cfn_ops_review_assistant.services.note_parser import NoteParser
from cfn_ops_review_assistant.services.crm_service import CRMService

'''Class to parse the notes extracted from the CRM API'''

def review(case_number, token) -> ReviewResult:
    process = CRMService()
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
    return ReviewResult(
            case_number=case_number,
            process_name="psr-review",
            status=comparison_result["match"],
            summary=summary,
            comparison_result=comparison_result,
            )
    