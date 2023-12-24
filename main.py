import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True