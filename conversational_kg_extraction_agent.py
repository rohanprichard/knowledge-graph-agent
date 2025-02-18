import os
import json
import rich
from rich.console import Console
import openai
import uuid
import instructor
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import requests
from pyvis.network import Network


load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

class Node(BaseModel):
    id: str
    label: str
    entity_type: str


class Edge(BaseModel):
    id: str
    source: Node
    target: Node
    label: str


class Graph(BaseModel):
    nodes: List[Node]
    edges: List[Edge]


class InferenceRequest(BaseModel):
    text: str
    graph: Graph


class InferenceResponse(BaseModel):
    response: str
    new_nodes: List[Node]
    new_edges: List[Edge]


with open("assets/prompts/task-prompt.txt", "r") as file:
    task_prompt = file.read()

console = Console()

console.print("\n\n\n")
console.rule("[bold green]Task Prompt[/bold green]")
console.print(task_prompt)
console.rule()
console.print("\n\n\n")

console.print("\n[bold green]Emma:[/bold green] Hi! What's your name?")
name = input("You: ")
console.print(f"\n[bold green]Emma:[/bold green] Hi, {name}! How can I help you today?")

user = Node(id=str(uuid.uuid4()), label=name, entity_type="person")
knowledge_graph = Graph(nodes=[user], edges=[])



client = instructor.from_openai(openai.OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com/v1"))


def get_response(text: str):
    response = client.completions.create(
        model="deepseek-chat",
        messages=[
        {"role": "system", "content": task_prompt.format(graph=knowledge_graph)},
        {"role": "user", "content": text},
        ],
        stream=False,
        response_model=InferenceResponse
        )
    return response

def visualize_graph(graph: Graph):
    nodes = graph.nodes
    edges = graph.edges

    net = Network(height="750px", width="100%", font_color="#ffffff",  bgcolor="#222222", directed=False)

    for node in nodes:
        node_id = node.id
        label = node.label
        title = node.label
        net.add_node(node_id, label=label, title=title)

    for edge in edges:
        source = edge.source.id
        target = edge.target.id
        label = edge.label
        net.add_edge(source=source, to=target, label=label)

    output_file = "knowledge_graph.html"
    net.save_graph(output_file)

def main_loop():
    while True:
        user_input = console.input("\n[bold blue]You: [/bold blue]")
        if user_input == "/exit":
            break
        
        response = get_response(user_input)
        console.print(f"\n[bold green]Emma: {response.response} [/bold green]")
        knowledge_graph.nodes.extend(response.new_nodes)
        knowledge_graph.edges.extend(response.new_edges)
        visualize_graph(knowledge_graph)

main_loop()