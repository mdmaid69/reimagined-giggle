import array
def get_bytes_from_array(array):
        return array.tobytes()
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True