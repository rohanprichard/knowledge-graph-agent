# Knowledge Graph Extraction Agent

This project demonstrates how to build intelligent agents that can extract and maintain knowledge graphs from conversations. It consists of two main POCs:


1. **Knowledge Graph Extraction Agent** - Extracts structured information from text

2. **Conversational Knowledge Graph Agent** - Maintains a knowledge graph during a conversation


## Overview


The project uses Large Language Models (LLMs) to extract structured information from unstructured text and visualize it as a knowledge graph. The agents can:

Extract entities and relationships from text
- Build and maintain a knowledge graph during conversations
- Visualize the knowledge graph using interactive HTML


## Requirements

- Python 3.9+
- DeepSeek API key (or another LLM provider)


## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory with your API key:

```bash
DEEPSEEK_API_KEY=your_api_key_here
```


## Project Structure

- `knowledge-graph-extraction-agent.ipynb` - Demonstrates basic knowledge graph extraction from text
- `conversational-kg-extraction-agent.ipynb` - Builds a conversational agent that maintains a knowledge graph
- `conversational_kg_extraction_agent.py` - Python script version of the conversational agent
- `assets/prompts/task-prompt.txt` - System prompt for the conversational agent


## Usage

Knowledge Graph Extraction
The knowledge-graph-extraction-agent.ipynb notebook demonstrates how to extract a knowledge graph from a static text. It:

- Takes an unstructured text input 
- Extracts entities and relationships
- Visualizes the knowledge graph


Conversational Knowledge Graph Agent
The conversational-kg-extraction-agent.ipynb notebook creates an interactive agent named "Emma" that:
Engages in conversation with the user
Extracts information about the user during the conversation
Builds and maintains a knowledge graph of user information
Visualizes the knowledge graph in real-time


Running the Conversational Agent
You can run the conversational agent in two ways:
Using the Jupyter Notebook:
Open conversational-kg-extraction-agent.ipynb
Run all cells
Interact with the agent in the notebook
Using the Python Script:
If you've made changes to the notebook, run the last cell to generate the Python script
Run the script from the command line:

```bash
python conversational_kg_extraction_agent.py
```

## Making Changes

If you want to modify the agent:

- Make your changes in the conversational-kg-extraction-agent.ipynb notebook
- Run the last cell to generate an updated Python script
- Run the script to test your changes


## Key Components

### Data Models

The project uses Pydantic models to define the structure of the knowledge graph:
- Node - Represents entities with labels and types
- Edge - Represents relationships between entities
- Graph - Contains nodes and edges
- InferenceResponse - The structured output from the LLM

### Visualization

The knowledge graph is visualized using:
- pyvis - Creates an interactive HTML visualization
- The visualization is saved as knowledge_graph.html and can be opened in any browser

### Example Usage

When you run the conversational agent, it will:
- Ask for your name
- Engage in conversation
- Extract information about you
- Build a knowledge graph
- Generate an interactive visualization of the graph

You can exit the conversation by typing /exit.

### Technical Details

- The agent uses the DeepSeek API for inference
- The instructor library is used to get structured outputs from the LLM
- The knowledge graph is updated in real-time as new information is discovered


## License

This project is open source and available for educational and personal use under the MIT license.
