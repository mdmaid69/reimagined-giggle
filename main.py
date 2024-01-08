import array
def get_list_from_array(array):
        return array.tolist()
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])