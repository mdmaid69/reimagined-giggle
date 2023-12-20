  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a