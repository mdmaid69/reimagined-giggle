def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity