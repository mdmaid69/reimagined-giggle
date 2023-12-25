import datetime
print(datetime.datetime.now())
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)