import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_average(lst):
        return sum(lst) / len(lst)