#! /bin/bash

# this test tests solhacker but not pyamf
# it requires the fake pyamf module in testdir

cd testdir

export PYTHONPATH="$PWD:$PYTHONPATH"

echo "test decode"
../solhacker <<< "solbinaryblob" > decode-actual.txt 2>&1
echo "('string', {'dict': 'solbinaryblob\n'})" > decode-expected.txt
diff decode-actual.txt decode-expected.txt

echo "test encode"
../solhacker <<< "('string', {'dict': 'wat'})" > encode-actual.txt 2>&1
echo "solobject:string{'dict': 'wat'}" > encode-expected.txt
diff encode-actual.txt encode-expected.txt

echo "test error"
../solhacker <<< "syntax error" > error-actual.txt 2>&1
echo "error: cannot decode nor encode" > error-expected.txt
diff error-actual.txt error-expected.txt

echo "test undefined"
../solhacker <<< "(u'foo', {u'bar': pyamf.Undefined})" > undefined-actual.txt 2>&1
echo "error: cannot encode pyamf.Undefined" > undefined-expected.txt
diff undefined-actual.txt undefined-expected.txt

