def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))