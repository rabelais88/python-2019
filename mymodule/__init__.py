def printfunc(arg):
  print(arg)

if __name__ == "__main__":
  print("this shouldn't be loaded as a program. please use it as a module")
  raise RuntimeError("module loaded as a pogram")