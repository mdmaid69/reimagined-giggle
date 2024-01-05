def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)