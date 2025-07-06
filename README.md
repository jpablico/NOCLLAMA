# NOCLLAMA 🦙

A local LLM-powered assistant to analyze, classify, and summarize data center NOC tickets and SOPs. Built with Ollama + LlamaIndex.

## Features

- Local-only, private by default (no OpenAI/API calls)
- Classifies ticket priority
- Summarizes long SOPs
- Redacts sensitive info
- Optional live integration with Chrome extension or API

## Requirements

- Python 3.10+
- Ollama (Mistral or LLaMA3)
- `pip install -r requirements.txt`

## Setup

```bash
cp .env.example .env
# Edit .env with your local paths