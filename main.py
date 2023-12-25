def calculate_area_circle(r):
        return 3.14 * r**2
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)