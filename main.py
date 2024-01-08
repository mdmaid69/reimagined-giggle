import collections
def create_queue():
        return collections.deque()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)