def main(num):
  if(num <= 0):
    return 0.53
  if(num == 1):
    return 0.19
  return (1 + (main(num - 2) ** 2 / 44) + (main(num - 1) / 76)) ** 3