import time
from cfn_ops_review_assistant.services.surface_helper import SurfaceAdapter
from cfn_ops_review_assistant.agent.observer import Observer

adapter = SurfaceAdapter()

adapter.launch_case(
    "24910726",
    "c24adfe3-c638-44a8-9681-8c056302af60",
)
time.sleep(5)

observer = Observer(adapter)

state = observer.observe()

print(state)