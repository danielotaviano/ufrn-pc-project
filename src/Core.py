from Args import Args
from NewException import NewException
from FileNames import FileNames
from Names import Names

class Core:
  def __init__(self):
    self.args = Args()
    self.exception = NewException(self.args)
    self.fileNames = FileNames(self.args)
    self.names = Names()

  def start(self):
    self.exception.throw()
    inputFileName, outputFileName = self.fileNames.getFileNames()
    self.names.read(inputFileName)
    self.names.sort()
    self.names.write(outputFileName)

    
