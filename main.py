def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import collections
def create_priority_queue():
        return collections.deque()