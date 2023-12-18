def find_common_elements(list1, list2):
        return set(list1) & set(list2)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))