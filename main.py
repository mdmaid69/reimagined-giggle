import array
def get_array_itemsize(array):
        return array.itemsize
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)