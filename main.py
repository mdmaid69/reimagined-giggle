import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5