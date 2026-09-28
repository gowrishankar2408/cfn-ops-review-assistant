# CFN Ops Review Assistant

A Python-based assistant for CFN operations review workflows, including PSR review and PPS custom expiration review capabilities.

## Project structure

- `capabilities/` contains review capability definitions and metadata.
- `src/cfn_ops_review_assistant/` holds the application package.
- `tests/` contains automated tests.
- `incidents/` stores screenshots, reports, and logs generated during investigations.

## Quick start

1. Create a virtual environment.
2. Install requirements.
3. Run the CLI entry point.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m cfn_ops_review_assistant.cli.app
```

## Environment

Configure the variables in `.env` before running the assistant.
