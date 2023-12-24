def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])