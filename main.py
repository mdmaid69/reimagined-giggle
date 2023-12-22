  def convert_to_binary(n):
        return bin(n)
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)