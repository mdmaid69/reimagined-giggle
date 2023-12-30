def calculate_speed(distance, time):
        return distance / time
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)