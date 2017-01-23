#! /bin/bash

echo "test decode"
./solhacker.py <<< "solbinaryblob" > delme-decode-actual.txt
echo "'fakepyamfdecode:solbinaryblob\n'" > delme-decode-expected.txt
diff delme-decode-actual.txt delme-decode-expected.txt

echo "test encode"
./solhacker.py <<< "('py', 'tuple')" > delme-encode-actual.txt
echo "fakepyamfencode:pytuple" > delme-encode-expected.txt
diff delme-encode-actual.txt delme-encode-expected.txt

