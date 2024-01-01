def reverse_list(lst):
        return lst[::-1]
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))