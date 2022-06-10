import math
# крч в каждой штуке на 1 уменьшаю, типо y(n+1 - [i/2]) === y(n - [i/2]) если в код переводить
def main(x, y, z):
    n = len(x)
    res = 0
    for i in range(1, n+1):
        temp = 0
        temp += y[int(n - math.ceil(float(i) / 2))]
        temp += z[i - 1] ** 3
        temp += 13 * x[int(n - math.ceil(float(i) / 2))] ** 2
        temp = math.exp(temp) ** 5
        temp *= 12
        res += temp
    return res * 84



print(main([0.28, 0.04, 0.56, -0.72],
[-0.33, 0.5, -0.31, -0.88],
[-0.57, -0.67, 0.52, 0.74]))

print(main([0.68, -0.07, 0.91, 0.34],
[-0.17, -0.8, 0.49, 0.53],
[0.19, -0.61, 0.28, -0.19]))