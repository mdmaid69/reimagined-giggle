def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def find_union(list1, list2):
        return set(list1) | set(list2)