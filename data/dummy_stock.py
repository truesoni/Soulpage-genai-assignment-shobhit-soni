# data/dummy_stock.py

import random

def get_stock_data(company_name: str):
    return {
        "current_price": random.randint(1, 250),
        "weekly_change": random.uniform(1, 70),
        "market_cap": "1.2T USD"
    }
