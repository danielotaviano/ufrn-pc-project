class Names:
  def __init__(self):
    self.names = []
  

  def read(self, inputFileName):
    f = open(inputFileName,'r')
    for name in f.read().split('\n'):
      self.names.append(name)

  def sort(self):
    self.names.sort()

  def write(self, outputFileNames):
    fs = open(outputFileNames, "w")
    for name in self.names:
      fs.write(name + '\n' )
    fs.close()