def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)