import array
def convert_array_to_unicode(array):
        return array.tounicode()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)