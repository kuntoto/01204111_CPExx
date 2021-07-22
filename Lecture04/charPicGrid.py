grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

def myPrint(g):
  for i in range(len(g)):
    for j in range(len(g[i])):
      print(f'{g[i][j]}', end='')
    print()

def rotateRight(g):
  print('Not implemented yet!')
  return None

def rotateLeft(g):
  print('Not implemented yet!')
  return None

myPrint(grid)
