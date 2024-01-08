def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a