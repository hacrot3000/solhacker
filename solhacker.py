#! /usr/bin/env python2

# converts a flash cookie (sol) to plaintext (python repr)
# requires pyamf

# expects input from stdin
# writes to stdout
# no arguments

import ast
import pprint
import sys

from pyamf import sol

def main():
  filecontent = sys.stdin.read()
  try:
    pytuple = sol.decode(filecontent)
    pprint.pprint(pytuple)
  except Exception:
    pytuple = ast.literal_eval(filecontent)
    solobject = sol.encode(pytuple[0], pytuple[1])
    sys.stdout.write(solobject.getvalue())

if __name__ == "__main__":
  main()
