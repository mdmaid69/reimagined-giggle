import array
def convert_array_to_bytes(array):
        return array.tobytes()
def calculate_roi(gain, cost):
        return (gain - cost) / cost