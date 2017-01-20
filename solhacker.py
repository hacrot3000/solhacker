#!/usr/bin/python

import ast
import os
import pprint
import sys

from pyamf import sol

# ------------------------------------------------------------------------------
def main():
  lines = "".join(sys.stdin.readlines())
  try:
    solobject = sol.decode(lines)
    pprint.pprint(solobject)
  except Exception:
    pyobject = ast.literal_eval(lines)
    solobject = sol.encode(pyobject[0], pyobject[1])
    sys.stdout.write(solobject.getvalue())

# ------------------------------------------------------------------------------
if __name__ == "__main__":
  main()
