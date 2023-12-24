def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import collections
def create_stack():
        return collections.deque()