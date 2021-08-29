def readScores():
  res = []
  with open('s.txt', 'r') as fp:
    i, header = 0, fp.readline().strip()
    #print(header)
    for line in fp:
      #print(f'{i+1},{line.strip()}')
      i += 1
      m = line.strip().split(',')
      if 'Agreement' not in m[0]: 
        res.append(int(m[7]))
  return res

def calStat(res):
  myMax,myMin,mySum,myDif = -100,100,0,0
  nbStd = len(res)
  for sc in res:
    if sc > myMax:
      myMax = sc
    if sc < myMin:
      myMin = sc
    mySum += sc
  myAvg = mySum / nbStd
  for sc in res:
    myDif += (sc - myAvg)**2
  myStd = (myDif/nbStd)**(0.5)
  print(nbStd)
  print(myMax, f'{myAvg:.2f}', f'{myStd:.2f}', myMin)
  
def calGrade(res):
  g = {}
  g['A'],g['B+'],g['B'],g['C+'] = 0,0,0,0 
  g['C'],g['D+'],g['D'],g['F'] = 0,0,0,0 
  gg = ['A','B+','B','C+','C','D+','D','F']
  for sc in res:
    perc = sc*100/40
    if perc > 85:
      g['A'] += 1 
    elif perc > 79:
      g['B+'] += 1 
    elif perc > 73:
      g['B'] += 1
    elif perc > 67:
      g['C+'] += 1 
    elif perc > 60:
      g['C'] += 1
    elif perc > 50:
      g['D+'] += 1
    elif perc > 40:
      g['D'] += 1 
    else:
      g['F'] += 1 
  for i in range(len(gg)):
    print(f'{gg[i]}: {g[gg[i]]}')

### main begins here
res = readScores()
#print(res)
calStat(res)
calGrade(res)