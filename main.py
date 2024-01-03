import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)