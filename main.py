def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b