import array
def get_bytes_from_array(array):
        return array.tobytes()
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)