def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)