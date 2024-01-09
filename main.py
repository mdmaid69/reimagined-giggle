import array
def get_bytes_from_array(array):
        return array.tobytes()
def calculate_roi(gain, cost):
        return (gain - cost) / cost