list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)