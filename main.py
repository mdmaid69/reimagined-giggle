def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)