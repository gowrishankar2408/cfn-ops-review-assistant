from pydantic import BaseModel


class CapabilityHealthResult(BaseModel):

    capability: str

    total_executions: int

    success_count: int

    failure_count: int

    log_file: str

    success_rate: float