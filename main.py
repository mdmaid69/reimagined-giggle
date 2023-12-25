import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_roi(gain, cost):
        return (gain - cost) / cost