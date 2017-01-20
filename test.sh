#! /bin/sh

echo "(u'foo', {u'bar': u'baz'})" > delme.py

./solhacker.sh delme.py < delme.py > delme.sol

./solhacker.sh delme.sol < delme.sol > delme2.py

diff delme.py delme2.py
