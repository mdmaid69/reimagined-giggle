def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_circumference_circle(r):
        return 2 * 3.14 * r