import sys
class Args:
  def get(self):
    argv = sys.argv.copy()
    argv.remove(argv[0])
    return argv