def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
def find_union(list1, list2):
        return set(list1) | set(list2)