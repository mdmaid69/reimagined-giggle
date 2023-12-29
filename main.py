def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import array
def get_bytes_from_array(array):
        return array.tobytes()