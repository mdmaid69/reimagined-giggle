import array
def convert_array_to_bytes(array):
        return array.tobytes()
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)