#! /bin/bash

# this test tests solhacker but not pyamf
# it requires the fake pyamf module in testdir

cd testdir

export PYTHONPATH="$PWD:$PYTHONPATH"

echo "test decode"
../solhacker <<< "solbinaryblob" > decode-actual.txt
echo "('string', {'dict': 'solbinaryblob\n'})" > decode-expected.txt
diff decode-actual.txt decode-expected.txt

echo "test encode"
../solhacker <<< "('string', {'dict': 'wat'})" > encode-actual.txt
echo "solobject:string{'dict': 'wat'}" > encode-expected.txt
diff encode-actual.txt encode-expected.txt

