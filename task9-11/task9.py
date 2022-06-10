from enum import Enum
from re import L

class main:
  currentLetter = "A"
  data = {
    "A": [
      {
        "letter": "B",
        "returned": 0,
        "method": "stall"
      }
    ],
    "B": [
      {
        "letter": "C",
        "returned": 1,
        "method": "stall"
      },
      {
        "letter": "D",
        "returned": 2,
        "method": "load"
      },
    ],
    "C": [
      {
        "letter": "F",
        "returned": 5,
        "method": "load"
      },
      {
        "letter": "H",
        "returned": 4,
        "method": "stall"
      },
      {
        "letter": "D",
        "returned": 3,
        "method": "hike"
      },
    ],
    "D": [
      {
        "letter": "E",
        "returned": 6,
        "method": "hike"
      }
    ],
    "E": [
      {
        "letter": "F",
        "returned": 7,
        "method": "load"
      },
      {
        "letter": "H",
        "returned": 8,
        "method": "stall"
      }
    ],
    "F": [
      {
        "letter": "G",
        "returned": 9,
        "method": "load"
      },
    ],
    "G": [
      {
        "letter": "H",
        "returned": 10,
        "method": "load"
      },
      {
        "letter": "A",
        "returned": 11,
        "method": "stall"
      },
    ],
    "H": []
  }
  def __init__(self):
    pass
  
  def makeAction(self, name):
    variants = self.data[self.currentLetter]
    for item in variants:
      if(item["method"] == name):
        self.currentLetter = item["letter"]
        return item["returned"]
    raise KeyError;
  
  def stall(self):
    return self.makeAction("stall")
  
  def hike(self):
    return self.makeAction("hike")
  
  def load(self):
    return self.makeAction("load")
    

# o = main()

# print(o.stall())

# print(o.stall())

# print(o.load())

# print(o.load())

# print(o.stall())

class main2:
  currentLetter = "A"
  data = {
    "A": [
      {
        "letter": "B",
        "returned": 0,
        "method": "fork"
      },
      {
        "letter": "G",
        "returned": 1,
        "method": "log"
      }
    ],
    "B": [
      {
        "letter": "C",
        "returned": 2,
        "method": "log"
      },
    ],
    "C": [
      {
        "letter": "D",
        "returned": 3,
        "method": "peep"
      },
    ],
    "D": [
      {
        "letter": "A",
        "returned": 5,
        "method": "peep"
      },
      {
        "letter": "E",
        "returned": 4,
        "method": "log"
      }
    ],
    "E": [
      {
        "letter": "F",
        "returned": 6,
        "method": "peep"
      },
      {
        "letter": "G",
        "returned": 7,
        "method": "fork"
      }
    ],
    "F": [
      {
        "letter": "G",
        "returned": 8,
        "method": "fork"
      },
      {
        "letter": "B",
        "returned": 9,
        "method": "peep"
      },
    ],
    "G": [
      {
        "letter": "H",
        "returned": 10,
        "method": "peep"
      },
    ],
    "H": [
      {
        "letter": "B",
        "returned": 11,
        "method": "fork",
      }
    ]
  }
  def __init__(self):
    pass
  
  def makeAction(self, name):
    variants = self.data[self.currentLetter]
    for item in variants:
      if(item["method"] == name):
        self.currentLetter = item["letter"]
        return item["returned"]
    raise KeyError;
  
  def peep(self):
    return self.makeAction("peep")
  
  def fork(self):
    return self.makeAction("fork")
  
  def log(self):
    return self.makeAction("log")
  
o2 = main2()



def createObj(letter, method, returned):
  return {
    "letter": letter,
    "method": method,
    "returned": returned
  }
  
def createMulti(items):
  return list(map(lambda x: createObj(x[0], x[1], x[2]), items))

class Method(Enum):
  Fork = "fork",
  Log = "log",
  Peep = "peep"
  
class Letter(Enum):
  A = "A",
  B = "B",
  C = "C",
  D = "D",
  E = "E",
  F = "F",
  G = "G",
  H = "H",
  

class main3:
  currentLetter = Letter.A
  data = {
    Letter.A: createMulti([[Letter.B,Method.Fork, 0], [Letter.G, Method.Log, 1]]),
    Letter.B: createMulti([[Letter.C,Method.Log, 2]]),
    Letter.C: createMulti([[Letter.D,Method.Peep, 3]]),
    Letter.D: createMulti([[Letter.E,Method.Log, 4], [Letter.A, Method.Peep, 5]]),
    Letter.E: createMulti([[Letter.F,Method.Peep, 6], [Letter.G, Method.Fork, 7]]),
    Letter.F: createMulti([[Letter.G,Method.Fork, 8], [Letter.B, Method.Peep, 9]]),
    Letter.G: createMulti([[Letter.H,Method.Peep, 10]]),
    Letter.H: createMulti([[Letter.B,Method.Fork, 11]]),
  }
  def __init__(self):
    pass
  
  def makeAction(self, name):
    variants = self.data[self.currentLetter]
    for item in variants:
      if(item["method"] == name):
        self.currentLetter = item["letter"]
        return item["returned"]
    raise KeyError;
  
  def peep(self):
    return self.makeAction(Method.Peep)
  
  def fork(self):
    return self.makeAction(Method.Fork)
  
  def log(self):
    return self.makeAction(Method.Log)
  
o3 = main3()

print(o3.fork()) # 0
print(o3.log()) # 2
print(o3.peep()) # 3
print(o3.log()) # 4
print(o3.peep()) # 6
print(o3.peep()) # 9
print(o3.log()) # 2
print(o3.peep()) # 3
print(o3.log()) # 4
print(o3.fork()) # 7
print(o3.peep()) # 10