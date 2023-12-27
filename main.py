def calculate_work(force, distance):
        return force * distance
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)