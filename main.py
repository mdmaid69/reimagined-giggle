import array
def get_array_buffer_info(array):
        return array.buffer_info()
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)