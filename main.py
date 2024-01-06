import array
def convert_array_to_string(array):
        return array.tostring()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)