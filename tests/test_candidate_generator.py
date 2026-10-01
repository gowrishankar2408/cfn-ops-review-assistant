from cfn_ops_review_assistant.discovery.candidate_generator import CandidateGenerator

result = CandidateGenerator().generate(
    capability_name="test_capability",
    current_version="1.0",
    artifact={},
    request_id="test_request_id",
    incident_id="test_incident_id",
    analysis={},
)
print(result)
