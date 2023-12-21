import array
def get_array_as_memoryview(array):
        return memoryview(array)
i = 0
while i < 5:
        print(i)
        i += 1