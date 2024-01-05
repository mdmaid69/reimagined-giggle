def find_union(list1, list2):
        return set(list1) | set(list2)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)