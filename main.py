import argparse
def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input")
        parser.add_argument("--output")
        return parser.parse_args()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)