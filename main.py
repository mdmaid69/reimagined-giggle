import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time