import collections
def create_queue():
        return collections.deque()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time