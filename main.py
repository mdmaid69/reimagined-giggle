list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time