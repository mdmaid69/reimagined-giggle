def calculate_payback_period(cash_flows):
        cumulative_cash_flow = 0
        for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
                return i
        return None
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))