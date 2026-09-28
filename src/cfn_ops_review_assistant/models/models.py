from pydantic import BaseModel


class ReviewResult(BaseModel):

    case_number: str

    process_name: str

    status: str

    summary: str