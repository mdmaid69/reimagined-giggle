def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
def find_union(list1, list2):
        return set(list1) | set(list2)