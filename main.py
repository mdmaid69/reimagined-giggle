import array
def get_array_typecode(array):
        return array.typecode
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)