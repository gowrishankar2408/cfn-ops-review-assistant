from abc import ABC
from abc import abstractmethod

from cfn_ops_review_assistant.models.models import ReviewResult


class Capability(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def version(self) -> str:
        pass

    @abstractmethod
    def execute(
        self,
        case_number: str,
        token: str,
    ) -> ReviewResult:
        pass