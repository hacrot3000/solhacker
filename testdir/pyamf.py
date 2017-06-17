# fake pyamf for testing
# useful only if used with the test script

# the real pyamf has a submodule named sol
# which has functions decode and encode
# here it is a class with static methods

# decode expects a sol object and returns a tuple of a string and a dict
# encode expects a string and a dict (the tuple) and returns a sol object

# decode throws an exception if input is not a sol object
# this behaviour is relied upon in the main program
# the test script sends the string sol in place of the sol object

class sol:

  @staticmethod
  def decode(solobject):
    if not solobject.startswith('sol'):
      raise Exception('fake pyamf decode exception')
    return ('fakepyamfdecode:', solobject)

  @staticmethod
  def encode(_string, _dict):
    return SolObject(_string, _dict)

class SolObject:

  def __init__(self, _string, _dict):
    self._string = _string
    self._dict = _dict

  def getvalue(self):
    return 'fakepyamfencode:' + self._string + self._dict + '\n'
