import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)