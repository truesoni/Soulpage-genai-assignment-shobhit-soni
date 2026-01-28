# agents/analyst.py
from state import CompanyState

def analyst_agent(state: CompanyState) -> CompanyState:
    company = state["company_name"]
    news = state["news"]
    stock = state["stock_data"]

    analysis = f"""
    📊 Company Intelligence Report

    Key Insights for {company}:
    - Recent news indicates positive momentum and innovation.
    - Market confidence reflected in recent stock movement.

    Stock Overview:
    - Current Price: {stock.get("current_price")}
    - Weekly Change: {stock.get("weekly_change")}
    - Market Cap: {stock.get("market_cap")}

    Risks:
    - High valuation could lead to correction.
    - Competitive pressure in core markets.
    """

    state["analysis"] = analysis.strip()
    return state
