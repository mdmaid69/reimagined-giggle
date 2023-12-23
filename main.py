def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_roi(gain, cost):
        return (gain - cost) / cost