def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)