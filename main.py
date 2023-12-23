import array
def get_array_item_count(array, item):
        return array.count(item)
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True