def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])