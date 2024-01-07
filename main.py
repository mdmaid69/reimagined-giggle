def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)