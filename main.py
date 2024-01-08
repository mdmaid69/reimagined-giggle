def find_common_elements(list1, list2):
        return set(list1) & set(list2)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])