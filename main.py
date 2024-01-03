import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)