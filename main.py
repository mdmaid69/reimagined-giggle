def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets