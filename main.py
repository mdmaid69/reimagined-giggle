import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)