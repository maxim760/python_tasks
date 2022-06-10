def main(a,m,n, y):
  res = 0
  for c in range(1, m + 1):
    for j in range(1, a + 1): 
      for k in range(1, n + 1):
        res += (k ** 7) - (y ** 6) - (45 * (c ** 2 - j ** 3))
  return res