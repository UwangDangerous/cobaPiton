import os
if os.path.exists("coba.txt"):
  os.remove("coba.txt")
else:
  print("The file does not exist")