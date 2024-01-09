def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets