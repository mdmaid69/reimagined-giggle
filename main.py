import array
def reverse_array(array):
        array.reverse()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)