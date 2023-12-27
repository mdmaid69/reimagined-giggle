  def convert_to_binary(n):
        return bin(n)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h