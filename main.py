def find_common_elements(list1, list2):
        return set(list1) & set(list2)
def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                return False
        return True