'''
  [Exam] สอบกี่ทีไม่ดีขึ้นเลย
'''

n = int(input('Number of inputs: '))
nameDic, nameCount = {}, {}
for i in range(n):
	name = input('Input name: ')
	sc = float(input('Input score: '))
	if name in nameDic.keys():
		nameDic[name] += sc
		nameCount[name] += 1
	else:
		nameDic[name] = sc
		nameCount[name] = 1
#print(nameDic)
#print(nameCount)

nameScore = {}
myMax, nMax = -999999, ''
for k,v in nameDic.items():
	nameScore[k] = v / nameCount[k]
	if nameScore[k] > myMax:
		myMax = nameScore[k]
		nMax = k
#print(nameScore, myMax)
print(f'Top score is {nMax}: {myMax:.2f}')


'''
  [mine_sweeper] แผนที่ระเบิด / just a sample proposal
'''
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
