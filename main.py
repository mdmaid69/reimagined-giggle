import array
def get_string_from_array(array):
        return array.tobytes()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])