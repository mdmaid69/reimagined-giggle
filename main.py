numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))