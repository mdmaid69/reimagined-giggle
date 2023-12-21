for i in range(10): print(i)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))