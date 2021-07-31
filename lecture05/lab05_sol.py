import copy

def printBoard(a):
  for i in range(len(a)):
    for j in range(len(a[i])):
      print(f'{a[i][j]:^3}', end='')
    print()
  print()

def checkMine(b):
  a =copy.deepcopy(b)
  r,c = len(a), len(a[0])
  for i in range(r):
    for j in range(c):
      if a[i][j] == 'X':
        #print(f'i={i},j={j}') 
        for p in range(i,r): #SE
          for q in range(j,c):
            if a[p][q] != 'X' and p<=i+1 and q<=j+1:
              a[p][q] += 1
        for p in range(i-1,-1,-1): #NE_BIS
          for q in range(j+1,c):
            if a[p][q] != 'X' and p>=i-1 and q<=j+1:
              a[p][q] += 1
        for p in range(i,-1,-1): #NW
          for q in range(j,-1,-1):
            if a[p][q] != 'X' and p>=i-1 and q>=j-1:
              a[p][q] += 1
        for p in range(i+1,r): #SW_BIS
          for q in range(j-1,-1,-1):
            if a[p][q] != 'X' and p<=i+1 and q>=j-1:
              a[p][q] += 1
  return a

a = [['X','X','X',0],[0,'X',0,0],[0,0,0,'X']]
printBoard(a)
b = checkMine(a)
printBoard(b)
