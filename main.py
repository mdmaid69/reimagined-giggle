import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)