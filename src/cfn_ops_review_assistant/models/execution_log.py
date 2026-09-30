from pydantic import BaseModel


class ExecutionLog(BaseModel):

    case_number: str

    capability: str

    version: str

    status: str

    result: str

    incident_id: str = None

    discovery_request_id: str = None

    timestamp: str