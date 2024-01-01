def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets