def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)