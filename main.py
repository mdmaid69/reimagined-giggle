def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))