def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity