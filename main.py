def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)