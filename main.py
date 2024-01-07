text = "Hello, world!"
print("Words:", len(text.split()))
import array
def get_array_as_memoryview(array):
        return memoryview(array)