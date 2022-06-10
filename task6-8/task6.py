x2Map = {
  2019: 12,
  2012: 13,
  1984: False
}

x13Map = {
  "STATA": 3,
  "ECL": 4,
  "OZ": {
    1969: 0,
    1979: 2,
    2003: 1
  }
}

x10Map = {
  "ECL": 11,
  "STATA": {
    1992: 8,
    2000: 9,
    1985: 10
  },
  "OZ": {
    1992: 5,
    2000: 6,
    1985: 7
  }
}

def getX4(x4, x3, x0, x1):
  [map, nextX] = [x13Map, x3] if x4 == 1986 else [x10Map, x0]
  try:
      return map[x1][nextX]
  except Exception:
      return map[x1]
  
def main(x):
  return x2Map[x[2]] or getX4(x[4], x[3], x[0], x[1])

print(main([1985, 'OZ', 2012, 1979, 1957]))
print(main([1985, 'OZ', 1984, 2003, 1957]))
print(main([1985, 'OZ', 2019, 1969, 1957]))
print(main([1992, 'STATA', 1984, 1969, 1957]))
print(main([1985, 'OZ', 1984, 2003, 1986]))