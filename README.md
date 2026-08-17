# Knowledge Graph Extraction Agent

Experiments that use LLMs to extract entities and relationships from text or a live conversation, then visualise the resulting graph.

## Included experiments

- `knowledge-graph-extraction-agent.ipynb` — extracts a graph from static text.
- `conversational-kg-extraction-agent.ipynb` — maintains a graph as a conversation develops.
- `conversational_kg_extraction_agent.py` — script version of the conversational flow.
- [Generated graph visualisation](knowledge_graph.html) — a static HTML artifact that opens locally in a browser.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with the provider key used by your chosen implementation, for example:

```env
DEEPSEEK_API_KEY=your_key_here
```

The notebooks may use a different provider configuration; inspect the selected notebook before running it. Never commit provider keys.

## Run

Open either notebook in Jupyter and run its cells, or execute:

```bash
python conversational_kg_extraction_agent.py
```

The conversational flow exits with `/exit` and emits a graph visualisation.

## Data safety

Use synthetic or non-sensitive conversations for demos. Text is sent to the configured LLM provider and generated HTML may contain the entities and relationships it extracted.

## License

MIT
