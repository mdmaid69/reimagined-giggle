def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue