import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)