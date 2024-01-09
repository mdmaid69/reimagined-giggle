import sys
def exit_program():
        sys.exit()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)