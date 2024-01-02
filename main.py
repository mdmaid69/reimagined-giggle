def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def remove_from_array(array, item):
        array.remove(item)