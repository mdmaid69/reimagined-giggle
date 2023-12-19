def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding