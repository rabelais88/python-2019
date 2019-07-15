class MyTown (object):
  def __init__(self, name="mytown", population=65000, size=12000):
    print("a town is initialized")
    self.name = name
    self.population = population
    self.size = size
  def explain(self, key):
    print(self.__dict__[key])

charlestown = MyTown()
charlestown.explain(key="name")

class CityWithHall (MyTown):
  def __init__(self, name="mytown", population=65000, size=12000, hallname="townhall"):
    super().__init__(name, population, size)
    self.hallname = hallname
  def explainHall(self):
    print(self.hallname);

tomstown = CityWithHall(name="tomstown", hallname="tom's townhall")
tomstown.explain(key="name")
tomstown.explain(key="hallname")
tomstown.explainHall()
