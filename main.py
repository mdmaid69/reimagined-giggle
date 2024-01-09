def find_difference(list1, list2):
        return set(list1) - set(list2)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)