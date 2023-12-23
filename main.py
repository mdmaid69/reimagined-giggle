def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)