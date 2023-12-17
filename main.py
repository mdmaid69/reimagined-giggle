import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
def calculate_work(force, distance):
        return force * distance