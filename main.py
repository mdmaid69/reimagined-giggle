import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
                return False
        return True