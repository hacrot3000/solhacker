# fake pyamf for testing

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
