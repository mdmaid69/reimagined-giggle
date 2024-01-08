import array
def get_array_typecode(array):
        return array.typecode
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True