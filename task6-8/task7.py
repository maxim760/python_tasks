from dataclasses import field
from functools import reduce
import math


def hexToBin(num):
    return bin(num)[2:]


def binToHexa(n):
  return hex(int(n, 2))


def main(num):
    binary = hexToBin(num).zfill(32)
    E = binary[0:1]
    D = binary[1:4]
    C = binary[4:13]
    B = binary[13:26]
    A = binary[26:32]
    newBinary = C + D + B + A + E
    # print(binary)
    # print(newBinary)
    newHex = binToHexa(newBinary).zfill(9)
    # print(newHex)
    return int(newHex, 16)

def generateMask(start, end):
  reverseStart = 31 - end
  reverseEnd = 31 - start
  return int (f'0b{"0" * reverseStart}{"1" * (reverseEnd - reverseStart + 1)}{"0" * start} ', 2)
def generateMaskWithInput(input, start, end):
  return input & generateMask(start, end)
def generateMaskWithInputAndOffset(input, offset, start, end):
  maskWithInput = generateMaskWithInput(input, start, end)
  return maskWithInput << offset if offset >= 0 else maskWithInput >> abs(offset)

def getResultBytes(input, data):
  fields = []
  for item in data:
    offset, start, end = item
    fields.append(generateMaskWithInputAndOffset(input, offset, start, end))
  return reduce(lambda x, y: x | y, fields)


def main2(input):
  a = generateMaskWithInputAndOffset(input, 1, 0, 5)
  b = generateMaskWithInputAndOffset(input, 1, 6, 18)
  c = generateMaskWithInputAndOffset(input, 4, 19, 27)
  d = generateMaskWithInputAndOffset(input, -8, 28, 30)
  e = generateMaskWithInputAndOffset(input, -31, 31, 31)
  return a | b | c | d | e

def main3(input):
  return getResultBytes(input, [
    [1, 0, 5],
    [1, 6, 18],
    [4, 19, 27],
    [-8, 28, 30],
    [-31, 31, 31]
  ])

print(main(0x4088f392))
print(main2(0x4088f392))
print(main3(0x4088f392))