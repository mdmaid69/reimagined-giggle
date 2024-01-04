n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))