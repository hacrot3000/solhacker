#!/usr/bin/python

import ast
import os
import pprint
import sys

from pyamf import sol

# ------------------------------------------------------------------------------
def sol2py(filename):
  lines = "".join(sys.stdin.readlines())
  solobject = sol.decode(lines)
  pprint.pprint(solobject)

# ------------------------------------------------------------------------------
def py2sol(filename):
  lines = "".join(sys.stdin.readlines())
  pyobject = ast.literal_eval(lines)
  solobject = sol.encode(pyobject[0], pyobject[1])
  sys.stdout.write(solobject.getvalue())

# ------------------------------------------------------------------------------
def main():

  filename = None
  try:
    filename = sys.argv[1]
  except:
    sys.stdout.write("needs filename as argument\n")
    sys.exit(2)

  filename = os.path.abspath(os.path.expanduser(filename))
  extension = filename.rpartition(".")[2]

  if extension == "sol":
    sol2py(filename)
  elif extension == "py":
    py2sol(filename)
  else:
    sys.stdout.write("extension must be .sol or .py\n")
    sys.exit(2)

# ------------------------------------------------------------------------------
if __name__ == "__main__":
  main()
