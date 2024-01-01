def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())