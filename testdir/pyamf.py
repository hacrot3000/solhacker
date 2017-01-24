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
  def decode(wat):
    if not wat.startswith('sol'):
      raise Exception('fake pyamf decode exception')
    return 'fakepyamfdecode:' + wat

  @staticmethod
  def encode(wat1, wat2):
    return SolObject(wat1, wat2)

class SolObject:

  def __init__(self, wat1, wat2):
    self.wat1 = wat1
    self.wat2 = wat2

  def getvalue(self):
    return 'fakepyamfencode:' + self.wat1 + self.wat2 + '\n'
