def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)