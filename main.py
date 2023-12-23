import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_volume(length, width, height):
        return length * width * height