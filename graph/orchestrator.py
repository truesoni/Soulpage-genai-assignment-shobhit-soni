# graph/orchestrator.py
from langgraph.graph import StateGraph
from state import CompanyState
from agents.data_collector import data_collector_agent
from agents.analyst import analyst_agent

def build_graph():
    graph = StateGraph(CompanyState)

    graph.add_node("data_collector", data_collector_agent)
    graph.add_node("analyst", analyst_agent)

    graph.set_entry_point("data_collector")
    graph.add_edge("data_collector", "analyst")
    graph.set_finish_point("analyst")

    return graph.compile()
