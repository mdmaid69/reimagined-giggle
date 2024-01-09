import array
def get_array_buffer_info(array):
        return array.buffer_info()
def calculate_roi(gain, cost):
        return (gain - cost) / cost