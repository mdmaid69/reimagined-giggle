n = 10
print("Cube numbers:", [x**3 for x in range(n)])
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))