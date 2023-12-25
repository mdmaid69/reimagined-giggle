def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)