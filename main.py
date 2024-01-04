def find_union(list1, list2):
        return set(list1) | set(list2)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time