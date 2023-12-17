def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
def find_common_elements(list1, list2):
        return set(list1) & set(list2)