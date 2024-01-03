import array
def set_array_item(array, i, item):
        array[i] = item
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)