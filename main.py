import collections
def create_stack():
        return collections.deque()
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time