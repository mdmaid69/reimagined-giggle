import array
def get_array_as_frozenset(array):
        return frozenset(array)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)