class NewException:
  def __init__(self,argv):
    self.argv = argv.get()

  def throw(self):
    if (not self.argv):
      raise Exception("Para executar o programa, passe os argumentos. ex: -i NomeDoArquivoDeOrigem.txt -o NomeDoArquivoDeSaida.txt") 
    if ('-i' not in self.argv):
      raise Exception("Para execução do programa, é obrigatório a passagem do arquivo de origem como argumento. ex: -i NomeDoArquivoDeOrigem.txt")