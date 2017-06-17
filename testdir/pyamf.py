# fake pyamf for testing
# useful only if used with the test script

# the real pyamf has a submodule named sol
# which has functions decode and encode
# here it is a class with static methods

# decode expects a sol object and returns a tuple of a string and a dict
# decode throws an exception if input is not a sol object
# in this test the "sol object" is a string that begins with "sol"

# encode expects a string and a dict (the tuple) and returns a sol object
# the sol object is defined by the method getvalue()

class DecodeError(Exception):
  pass

class sol:

  @staticmethod
  def decode(solobject):
    if not solobject.startswith('sol'):
      raise DecodeError('fake pyamf decode exception')
    return ('string', {'dict': solobject})

  @staticmethod
  def encode(_string, _dict):
    class SolObject:
      def __init__(self, _string, _dict):
        self._string = _string
        self._dict = _dict
      def getvalue(self):
        return 'solobject:' + self._string + repr(self._dict) + '\n'
    return SolObject(_string, _dict)

