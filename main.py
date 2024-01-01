import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"