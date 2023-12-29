def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)