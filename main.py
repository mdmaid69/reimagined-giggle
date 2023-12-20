def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets