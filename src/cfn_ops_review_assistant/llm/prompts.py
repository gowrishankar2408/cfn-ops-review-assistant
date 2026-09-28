"""Prompt templates for model interaction."""

from __future__ import annotations

COMPARISON_PROMPT_TEMPLATE = """
You are a compliance review engine.

Your job is to determine whether two disclosure notes represent an exact business match.

IMPORTANT RULES:
1. Ignore only these fields:
   - ORIGINAL SUBMIT DATE
   - EDIT SUBMIT DATE
2. Treat all other fields as business-critical.
3. If ANY business-critical field differs, the result must be NO.
4. Do not assume records match because they appear similar.
5. Do not ignore small differences.
6. Do not assume typographical differences are acceptable.
7. A change in any of the following fields must result in NO:
   - ACCOUNT NUMBER
   - BROKER DEALER NAME
   - NAME OF FIRM
   - ACCOUNT TYPE
   - ACCOUNT OWNER
   - RELATIONSHIP TO ACCOUNT OWNER
   - ACCOUNT STATUS
   - TRANSACTION SOURCE
   - BILLING STATUS
   - COST CENTER
8. Return YES only if all business-critical fields match exactly.
9. Do not provide explanations unless differences are found.

Return JSON only in the format:
{{
  "match": "Matching|Not Matching",
  "differences": [
    "field_name"
  ]
}}

SECTION_A:
{left_clean}

SECTION_B:
{right_clean}
""".strip()
