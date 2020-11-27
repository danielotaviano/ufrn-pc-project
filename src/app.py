from Core import Core

core = Core()

try:
  core.start()
except Exception as e:
  print(str(e)) 
