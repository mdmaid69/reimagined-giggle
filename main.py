import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import sys
def exit_program():
        sys.exit()