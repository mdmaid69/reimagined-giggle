def remove_duplicates(lst):
        return list(set(lst))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b