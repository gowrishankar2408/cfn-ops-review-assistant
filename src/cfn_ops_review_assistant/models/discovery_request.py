from pydantic import BaseModel

class DiscoveryRequest(BaseModel):

    request_id: str

    capability: str

    version: str

    incident_id: str

    case_number: str

    status: str

    created_at: str