import array
def get_array_as_bytearray(array):
        return bytearray(array)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)