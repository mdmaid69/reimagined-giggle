import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def calculate_speed(distance, time):
        return distance / time