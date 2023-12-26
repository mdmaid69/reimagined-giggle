def find_common_elements(list1, list2):
        return set(list1) & set(list2)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)