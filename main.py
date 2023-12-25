import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)