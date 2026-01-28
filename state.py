# state.py
from typing import TypedDict, List, Dict

class CompanyState(TypedDict):
    company_name: str
    news: List[str]
    stock_data: Dict
    analysis: str
