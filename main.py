import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)