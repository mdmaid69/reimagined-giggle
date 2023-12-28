import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_perpetuity(payment, rate):
        return payment / rate