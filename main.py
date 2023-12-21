def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
def find_common_elements(list1, list2):
        return set(list1) & set(list2)