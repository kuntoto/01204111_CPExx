def createBlankMat(n):
  return [[0 for j in range(n)] for i in range(n)]

def printMat(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      print(f'{m[i][j]:>2}', end='')
    print()
  print()

def heavyRotate(m):
  n,k = len(m)//2+1, len(m)
  for p in range(n):
    nn = n - p
    #print(f'nn: {nn}')
    for i in range(k-2*p):
      for j in range(k-2*p):
        m[i+p][j+p] = nn
    #printMat(m)
  return m

## main begins here
n = int(input('Enter n: '))
k = 2*n -1
m = createBlankMat(k)
printMat(heavyRotate(m))
