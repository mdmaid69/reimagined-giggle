def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])