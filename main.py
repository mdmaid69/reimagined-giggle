import array
def get_array_item(array, i):
        return array[i]
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)