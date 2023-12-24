list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))