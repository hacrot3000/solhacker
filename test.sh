#! /bin/bash

# this test tests solhacker but not pyamf
# it requires the fake pyamf module in testdir

cd testdir

export PYTHONPATH="$PWD:$PYTHONPATH"

echo "test decode"
../solhacker.py <<< "solbinaryblob" > decode-actual.txt
echo "'fakepyamfdecode:solbinaryblob\n'" > decode-expected.txt
diff decode-actual.txt decode-expected.txt

echo "test encode"
../solhacker.py <<< "('py', 'tuple')" > encode-actual.txt
echo "fakepyamfencode:pytuple" > encode-expected.txt
diff encode-actual.txt encode-expected.txt

