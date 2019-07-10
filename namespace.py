global myvar
myvar = 3

def access_global1():
  # global variable is not accessible without explicit definitions
  myvar = "changed"
access_global1()
print(myvar)

def access_global2():
  global myvar # global variable is now accessible
  myvar = "changed again"
access_global2()
print(myvar)