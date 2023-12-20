def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets