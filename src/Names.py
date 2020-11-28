from Log import Log
class Names:
  def __init__(self):
    self.names = []
  

  def read(self, inputFileName):
    Log.message('Lendo o Arquivo...')
    f = open(inputFileName,'r',encoding = 'utf8')
    for name in f.read().split('\n'):
      self.names.append(name)

  def sort(self):
    Log.message('Organizando os nomes...')
    self.names.sort()

  def write(self, outputFileNames):
    Log.message('Escrevendo os nomes organizados...')
    fs = open(outputFileNames, "w", encoding = 'utf8')
    for name in self.names:
      fs.write(name + '\n' )
    fs.close()