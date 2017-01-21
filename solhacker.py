#!/usr/bin/python

import ast
import pprint
import sys

from pyamf import sol

def main():
  filecontent = sys.stdin.read()
  try:
    solobject = sol.decode(filecontent)
    pprint.pprint(solobject)
  except Exception:
    pyobject = ast.literal_eval(filecontent)
    solobject = sol.encode(pyobject[0], pyobject[1])
    sys.stdout.write(solobject.getvalue())

if __name__ == "__main__":
  main()
