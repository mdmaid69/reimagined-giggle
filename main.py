def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)