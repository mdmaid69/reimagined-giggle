numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a