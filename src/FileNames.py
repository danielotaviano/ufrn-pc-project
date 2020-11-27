class FileNames:
  def __init__(self,args):
    self.args = args
    self.inputFileName = ''
    self.outputFileName = ''
  
  def getFileNames(self):
    argv = self.args.get()

    for e,i in enumerate(argv):
      if (i == '-i'):
        self.inputFileName = argv[e+1]
      if (i == '-o'):
        self.outputFileName = argv[e+1]

    if (not self.outputFileName):
      self.outputFileName = f'sort_{self.inputFileName}'

    return self.inputFileName, self.outputFileName
    


