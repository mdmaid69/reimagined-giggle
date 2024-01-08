import array
def append_to_array(array, item):
        array.append(item)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)