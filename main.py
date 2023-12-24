import array
def get_array_as_str(array):
        return str(array)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)