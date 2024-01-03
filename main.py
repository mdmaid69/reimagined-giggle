def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
def find_common_elements(list1, list2):
        return set(list1) & set(list2)