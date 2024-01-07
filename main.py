def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)