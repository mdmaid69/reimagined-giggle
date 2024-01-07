import array
def get_array_as_float(array):
        return float(array[0])
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)