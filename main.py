def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a