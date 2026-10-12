from cfn_ops_review_assistant.services.surface_helper import SurfaceAdapter


class Observer:

    def __init__(
        self,
        adapter: SurfaceAdapter,
    ):
        self.adapter = adapter

    def observe(self) -> dict:

        return {
            "url": self.adapter.capture_url(
                "agent-session"
            ),
            "controls": self.adapter.get_visible_controls(),
        }