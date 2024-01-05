import array
def get_array_as_memoryview(array):
        return memoryview(array)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)