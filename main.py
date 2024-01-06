import collections
def create_queue():
        return collections.deque()
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time