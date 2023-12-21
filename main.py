def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a