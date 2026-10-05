# CFN Ops Review Assistant
## Overview
CFN Ops Review Assistant is an AI-assisted capability platform designed to automate operational review workflows through deterministic replay, incident-driven discovery, and capability evolution.
## Problem Statement
Operational automations frequently fail when underlying applications evolve. Traditional automation solutions require manual updates whenever a UI control, locator, workflow step, or validation checkpoint changes.
CFN Ops Review Assistant addresses this challenge by implementing a capability-driven lifecycle:
Replay → Failure → Discovery → Capability Evolution → Replay
This enables the platform to detect failures, generate reusable capability updates, and continuously improve automation reliability while keeping humans in control of production changes.
The platform combines:
-	Deterministic execution for production workloads
-	Playwright-based UI automation
-	CRM API integrations
-	AI-assisted discovery and capability analysis
-	Versioned capability artifacts
-	Incident management and evidence collection
-	Human-in-the-loop approvals
-	Capability publishing and lifecycle management
#Solution Principle: 
Discover  Capability  Replay where AI is responsible for discovering and evolving capabilities, while production execution relies on deterministic replay.
# Architecture
## Production Execution Path
End User  CFN Ops Review Assistant Execution Manager Capability Registry Replay Engine Capability  Review Result Human Approval Case Closure
## Discovery Path
Support Team  Incident Screenshot + Evidence Discovery Request Discovery Engine Discovery Context LLM Analysis  Artifact Change Proposal Candidate Capability Support Approval Publish Capability Registry Updated Replay Uses Latest Version
# Supported Capabilities
## PSR Review
Reviews and compares original and edited CRM case notes using AI-assisted comparison.
### Workflow
Case Number → Generate CFN Session → Retrieve CRM Notes → Extract Original Note → Extract Edited Note → AI Comparison → Review Summary → Human Approval → Close Case
###Input
{ "case_number": "string"}
###Output
{
  "comparison_result": "Matching | Not Matching",
  "differences": []
}
## PPS Custom Expiration Review
Automates BOS review updates using Playwright.
### Workflow
Case Number → Generate CFN Session → Inject Session Cookie → Open BOS Case → Replay Capability → Validation → Review Summary → Human Approval → Close Case
### Inputs
{  "case_number": "string"}
### Outputs
{  "status": "Pass | Fail"}
###Capability Lifecycle
Current Version → Replay → Failure → Incident → Discovery Request → Discovery Context → LLM Discovery Analysis → Artifact Change Proposal → Candidate Capability → Support Review → Publish → Metadata Updated → Replay Uses New Version
### Capability Artifact Structure
Example:
{"name":"pps-custom-expiration","version":"2.0","inputs":{"case_number":"string"},"outputs":{"status":"string"},"steps":[{"action":"click","target":{"role":"link","name":"Edit"}},{"action":"check","target":{"role":"checkbox","name":"Exception Granted"}},{"action":"click","target":{"role":"button","name":"Update Case"}}],"checkpoint":{"text":"Exception Granted on Case"}}
# Discovery Engine
The Discovery Engine analyzes capability failures and proposes capability modifications.
### Discovery Inputs
-	Discovery Request
-	Incident Report
-	Screenshot Evidence
-	Capability Artifact
-	Failed Step
-	Visible Controls
-	Current URL
### Discovery Outputs
{"failure_type":"UI Drift","artifact_changes":[{"current":{},"proposed":{}}]}
# Candidate Capability Generation
Discovery analysis produces candidate capabilities for support review.
Example:
{"name":"pps-custom-expiration","version":"2.0","status":"candidate","generated_from":{"request_id":"DISC-001","incident_id":"INC-001"},"analysis":{"..."}}
Candidates are reviewed before publication.
## Example Capability Evolution
Capability v1
Expected Locator: Validate
Actual UI: Edit
Replay Result:
Fail
Discovery Result:
{
  "current": "Validate",
  "proposed": "Edit"
}
Candidate Capability v2 Generated
Capability v2 Published
Replay Result:
Pass
# Capability Publish workflow
Support publishes approved capabilities.
### Workflow
Candidate Capability → Approval → Publish → Metadata Updated → Replay Uses New Version
Metadata Example:
{  "name": "pps-custom-expiration",  "latest_version": "2.0",  "status": "active"}
# Incident Management
When replay fails:
	Replay Failure → Incident → Screenshot Evidence → Discovery Request
### Captured Evidence
-   Capability Name
-	Capability Version
-	Case Number
-	Failed Step
-	Error
-	Screenshot
-	Visible Controls
-	Current URL
-	Timestamp

# Human-in-the-Loop Governance
## Operations User
Responsibilities:
-	Run Reviews
-	Review Results
-	Approve Case Closure
## Support Team
Responsibilities:
-	Review Incidents
-	Run Discovery
-	Review Candidate Capabilities
-	Publish New Capability Versions
-	Production users never modify capabilities directly.
# Technology Stack
-	Python
-	Playwright
-	Ollama
-	Llama 3.1
-	REST APIs
-	Pydantic
-	JSON Capability Artifacts
-	Capability Registry
-	Replay Engine
-	GitHub
# Installation
## Clone Repository
“””bash
git clone <repository-url>“””
## Create Virtual Environment
“””bash
python -m venv .venv
“””
## Activate Environment
### Windows
“””powershell
.venv\Scripts\Activate.ps1
“””
### Linux / macOS
“””bash
source .venv/bin/activate
“””
## Install Dependencies
“””bash
pip install -e .
“””
## Setup Environment
“””bash
cfn-ops-review-assistant setup
“””
# Running Reviews
## Interactive Mode
“””bash
cfn-ops-review-assistant
“””
## PSR Review
“””bash
cfn-ops-review-assistant review \
  --review-type psr-review \
  --case-number 24910726
“””
## PPS Review
“””bash
cfn-ops-review-assistant review \
  --review-type pps-custom-expiration \
  --case-number 24910726
“””
# Discovery
## Run Discovery
“””
bash
cfn-ops-review-assistant discover \
  --request-id DISC-xxxxxxxx
“””
# Publish
“””
bash
cfn-ops-review-assistant publish \
  --request-id DISC-xxxxxxxx \
  --capability pps-custom-expiration“””
# Demonstrated End-to-End Capability Evolution
### Scenario 1
Capability expects: “Validate”
Application changed to: “Edit”
Replay fails.
Discovery identifies:
Validate → Edit
Candidate capability generated.
Support approves and publishes.
Replay uses the new artifact and succeeds.
### Scenario 2
Capability expects: “Update Notes”
Application changed to: “Update Case”
Replay fails.
Discovery identifies:
Update Notes → Update Case
Candidate capability generated.
Support approves and publishes.
Replay uses the new artifact and succeeds.
# Project Outcome
The platform demonstrates:
	Replay Failure → Discovery → AI Analysis → Artifact Change Proposal → Candidate Capability
