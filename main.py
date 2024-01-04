def calculate_area(radius):
        return 3.14 * radius * radius
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)