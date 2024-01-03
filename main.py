import array
def check_if_array_contains_item(array, item):
        return item in array
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)