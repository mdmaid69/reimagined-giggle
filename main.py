import array
def get_string_from_array(array):
        return array.tobytes()
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b