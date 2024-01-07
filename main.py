import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h