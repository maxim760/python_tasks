import math;

def calc1(x):
  return x ** 6 + 87 * x ** 2 + 34 * x ** 4

def calc2(x):
  return 52 * x - (math.sin(x) ** 6) / 40 - (x ** 3) / 37;

def calc3(x):
  return 98 * (1 + x ** 3) + math.asin(49 * x ** 3 - 24) ** 6

def main(x): 
  if(x < 44):
    return calc1(x)
  if(x < 97):
    return calc2(x)
  return calc3(x)

print(main(48))