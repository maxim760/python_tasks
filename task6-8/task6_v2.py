# если скажет, что много ифов
# то можно что такое
zeroMap = {
  1992: 0,
  2000: 1,
  1985: 2
}
def zero_v2(items, left, middle, right):
  return [left, middle, right][zeroMap[items[0]]]

def zero(items, left, middle, right):
  if(items[0] == 1992):
    return left
  if(items[0] == 2000):
    return middle
  return right

def one(items, left, middle, right):
  item = items[1]
  if(item == "OZ"): 
    return left
  if(item == "STATA"):
    return middle
  return right

def two(items, left, middle, right):
  item = items[2]
  if(item == 1984):
    return left
  if(item == 2019):
    return middle
  return right

def three(items, left, middle, right):
  item = items[3]
  if(item == 1969):
    return left
  if(item == 2003):
    return middle
  return right

def four(items, left, right): 
  if(items[4] == 1986):
    return left
  return right

def main(items):
  return two(
    items,
    four(
      items,
      one(
        items,
        three(
          items,
          0,
          1,
          2
        ),
        3,
        4
      ),
      one(
        items,
        zero(
          items,
          5,
          6,
          7
        ),
        zero(
          items,
          8,
          9,
          10
        ),
        11
      )
    ),
    12,
    13
  )
  
def main2(items):
  return two(
    items,
    four(
      items,
      one(
        items,
        three(
          items,
          0,
          1,
          2
        ),
        3,
        4
      ),
      one(
        items,
        zero_v2(
          items,
          5,
          6,
          7
        ),
        zero_v2(
          items,
          8,
          9,
          10
        ),
        11
      )
    ),
    12,
    13
  )
  
print(main([1985, 'OZ', 2012, 1979, 1957]))
print(main2([1985, 'OZ', 2012, 1979, 1957]))
print(main([1985, 'OZ', 1984, 2003, 1957]))
print(main2([1985, 'OZ', 1984, 2003, 1957]))
print(main([1985, 'OZ', 2019, 1969, 1957]))
print(main2([1985, 'OZ', 2019, 1969, 1957]))
print(main([1992, 'STATA', 1984, 1969, 1957]))
print(main2([1992, 'STATA', 1984, 1969, 1957]))
print(main([1985, 'OZ', 1984, 2003, 1986])) 
print(main2([1985, 'OZ', 1984, 2003, 1986])) 