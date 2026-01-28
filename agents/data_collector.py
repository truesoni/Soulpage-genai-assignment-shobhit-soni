# agents/data_collector.py
from state import CompanyState
from data.dummy_news import get_company_news
from data.dummy_stock import get_stock_data

def data_collector_agent(state: CompanyState) -> CompanyState:
    company = state["company_name"]

    state["news"] = get_company_news(company)
    state["stock_data"] = get_stock_data(company)

    return state
