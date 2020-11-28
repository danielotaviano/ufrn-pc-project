from termcolor import colored, cprint

class Log:
  def message(message):
    cprint('[Log] >> Message: '+message, 'green')

  def exception(message):
    cprint('[Log] >> ERROR: '+ message, 'red')