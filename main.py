  def convert_to_binary(n):
        return bin(n)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)