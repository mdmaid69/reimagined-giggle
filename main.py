import array
def clear_array(array):
        array *= 0
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)