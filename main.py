import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)