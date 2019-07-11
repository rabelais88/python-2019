from test import *
import mymodule
if __name__ == "__main__": # if loaded as a program
  testme('print this')
  mymodule.printfunc('hello!')
else:
  # don't do anything if loaded as a module
  print('this is a module')