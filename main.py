import array
def get_array_as_memoryview(array):
        return memoryview(array)
def calculate_roi(gain, cost):
        return (gain - cost) / cost