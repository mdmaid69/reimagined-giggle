import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)