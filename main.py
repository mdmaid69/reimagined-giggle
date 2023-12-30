n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity