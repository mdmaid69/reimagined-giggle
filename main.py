n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
def find_difference(list1, list2):
        return set(list1) - set(list2)