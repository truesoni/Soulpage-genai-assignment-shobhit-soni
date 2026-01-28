# main.py
from graph.orchestrator import build_graph

def main():
    app = build_graph()

    initial_state = {
        "company_name": input(), #getting input for company_name from user 
        "news": [],
        "stock_data": {},
        "analysis": ""
    }

    result = app.invoke(initial_state)
    print(result["analysis"])

if __name__ == "__main__":
    main()
