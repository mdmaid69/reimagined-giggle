import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)