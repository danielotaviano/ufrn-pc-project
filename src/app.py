from Core import Core
from Log import Log


core = Core()

try:
  core.start()
except Exception as e:
  Log.exception(str(e))

