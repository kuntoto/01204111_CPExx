def createMat(m,n):
  res, c = [], 1
  for i in range(m):
    tmp = []
    for j in range(n):
      tmp.append(c)
      c += 1 
    res.append(tmp)
  return res

def printMat(a):
  for i in range(len(a)):
    s = ''
    for j in range(len(a[i])):
      s += f'{a[i][j]:>3} '
    print(s)
  #print()
    
def browse(a, DEBUG=False):
  m,n = len(a), len(a[0])
  res = []
  for i in range(m-1):
    for j in range(n-1):
      tmp1 = []
      for p in range(2):
        tmp2 = []
        for q in range(2):
          if DEBUG: print(f'{a[i+p][j+q]:<3} ', end='')
          tmp2.append(a[i+p][j+q])
        if DEBUG: print()
        tmp1.append(tmp2)
      if DEBUG: print()
      res.append(tmp1)
      #land_price = tmp1[0][0] + (tmp1[0][1]*1.1) + (tmp1[1][1]*1.1) + (tmp1[1][0]*1.1*1.1)
      #print(f'{land_price:.2f}')
  #print(res)
  return res
        
### main begins here
a = createMat(2,3)
printMat(a)
tmp = browse(a)
for i in tmp:
  printMat(i)
  land_price = i[0][0] + (i[0][1]*1.1) + (i[1][1]*1.1) + (i[1][0]*1.1*1.1)
  print(f'{land_price:.2f}')
