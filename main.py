import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)