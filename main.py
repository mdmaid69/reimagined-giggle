import array
def iterate_over_array(array):
        for item in array:
        print(item)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a