import array
def extend_array(array, iterable):
        array.extend(iterable)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)