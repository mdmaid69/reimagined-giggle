import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)