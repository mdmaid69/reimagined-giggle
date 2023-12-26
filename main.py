def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array