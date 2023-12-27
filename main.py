def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)