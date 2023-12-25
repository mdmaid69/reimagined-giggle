def find_union(list1, list2):
        return set(list1) | set(list2)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])