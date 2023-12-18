def count_words(sentence):
        return len(sentence.split())
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)