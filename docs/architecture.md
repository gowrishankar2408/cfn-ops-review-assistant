# Architecture

This project provides an operational review assistant for CloudFormation change validation. It coordinates a capability registry, execution manager, and review processes for policy, exception, and expiration scenarios.

## Components

- `src/cfn_ops_review_assistant/cli` handles entry points and command execution.
- `src/cfn_ops_review_assistant/execution` coordinates workflow execution.
- `src/cfn_ops_review_assistant/processes` implements review-specific logic.
- `src/cfn_ops_review_assistant/services` wraps external dependencies such as CRM, notification, and token handling.
- `src/cfn_ops_review_assistant/llm` manages LLM interactions.
- `src/cfn_ops_review_assistant/incidents` collects evidence and manages incident artifacts.

## Design goals

- Keep capabilities modular and discoverable via metadata.
- Support deterministic review execution with replay and evidence collection.
- Provide a thin CLI for user-driven or scheduled orchestration.
