"""Discovery engine placeholder."""


class DiscoveryEngine:
    """Collects context needed for incidents or review execution."""

    def discover(self, query: str) -> dict:
        return {"query": query, "status": "not_implemented"}
