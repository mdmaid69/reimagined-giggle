def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)