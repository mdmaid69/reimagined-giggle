n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity