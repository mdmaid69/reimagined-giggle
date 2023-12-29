def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)