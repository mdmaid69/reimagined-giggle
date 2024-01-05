def calculate_power(work, time):
        return work / time
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)