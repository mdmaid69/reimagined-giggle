import array
def get_array_index(array, item):
        return array.index(item)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)