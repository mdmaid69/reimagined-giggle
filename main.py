import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def count_words(sentence):
        return len(sentence.split())