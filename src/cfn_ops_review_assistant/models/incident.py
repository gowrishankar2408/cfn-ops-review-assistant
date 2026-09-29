from pydantic import BaseModel


class Incident(BaseModel):

    incident_id: str

    capability: str

    version: str

    case_number: str

    error: str

    timestamp: str

    screenshot: str | None = None