import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal