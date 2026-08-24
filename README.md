# AI CRM Automation Portfolio

A practical portfolio work sample for AI adoption, CRM automation and systems-implementation roles.

The project models how Claude/OpenAI-style LLM features can be wired into CRM and no-code automation workflows without becoming a bolt-on chatbot. It is built around real business tasks named across AI/CRM job ads George is targeting: GoHighLevel-style pipeline setup, Zapier-style automation repair, client onboarding notes, landing-page/email funnel planning, dashboard snapshots, proposal QA, site assessment summaries, bill/data extraction, retrieval over approved knowledge, structured CRM records, privacy guardrails, evaluation, model benchmarking and human review.

## Why this exists

AI adoption roles are usually won or lost in the messy middle: CRM records are inconsistent, pipeline stages are unclear, automations break silently, clients need plain-English guidance, and leadership needs dashboards that show what is happening. This repo demonstrates the architecture I would use before touching production data:

- protect customer/site data before model calls
- retrieve from approved company knowledge instead of guessing
- force structured JSON outputs for CRM updates
- benchmark Claude/OpenAI-style models by accuracy, latency and estimated cost
- keep a human approval point for proposals, compliance and customer-facing records
- log decisions so the system is auditable
- translate technical workflow outputs into client-friendly onboarding steps

## Demo workflows

```bash
python app.py --workflow proposal_qa
python app.py --workflow site_summary
python app.py --workflow bill_extract
python app.py --workflow ghl_onboarding
python app.py --workflow zapier_repair
python app.py --workflow email_funnel
python app.py --workflow dashboard_snapshot
python evals/run_evals.py
```

The demo runs without external API keys. `src/llm_clients.py` contains provider interfaces and a deterministic local mock so the workflow can be reviewed safely.

## Project structure

```text
app.py                         CLI entrypoint
src/privacy.py                 PII and sensitive-site-data redaction
src/retrieval.py               lightweight retrieval over approved knowledge
src/workflows.py               CRM workflow orchestration
src/schemas.py                 structured output contracts
src/llm_clients.py             OpenAI/Anthropic provider interfaces + local mock
src/benchmark.py               cost/latency/quality comparison
evals/run_evals.py             task-level evaluation harness
data/knowledge/*.md            sample product/install/compliance knowledge
data/crm_records/*.json        sample CRM records
```

## What a reviewer should notice

- The workflows are not generic chat prompts. Each one has an expected CRM update, risk flags, evidence sources and a human-review boundary.
- GoHighLevel and Zapier are represented as structured operating concepts: pipelines, tags, triggers, workflow steps, broken automation diagnosis, onboarding tasks and reporting metrics.
- The output is intentionally boring in the best way: structured, auditable and safe enough to hand to a manager or client after human review.
- The project runs locally without API keys, which makes it safe to inspect, but the provider interface shows where Claude, Claude Code, OpenAI or other model providers would plug in.

## Production notes

A real deployment would replace the mock provider with Claude/OpenAI API calls, add queue workers for long document jobs, persist audit logs to the CRM database, use managed secrets, enforce role-based access, integrate with GoHighLevel/Zapier APIs, and run evals before every prompt/model change.
