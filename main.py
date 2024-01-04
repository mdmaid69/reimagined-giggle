def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h