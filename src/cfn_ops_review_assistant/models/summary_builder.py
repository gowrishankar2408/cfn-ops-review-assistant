class SummaryBuilder:

    def build(
        self,
        case_number: str,
        comparison_result: dict,
    ) -> str:

        match_status = comparison_result["match"]

        differences = comparison_result.get(
            "differences",
            [],
        )

        difference_text = (
            "\n".join(
                f"- {item}"
                for item in differences
            )
            if differences
            else "None"
        )

        return f"""
PSR Review Summary
--------------------------------------------------

Case Number:
{case_number}

Comparison Result:
{match_status}

Differences:
{difference_text}
"""
