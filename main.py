def find_difference(list1, list2):
        return set(list1) - set(list2)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)