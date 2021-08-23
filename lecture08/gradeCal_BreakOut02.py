def getSubGrade():
  subGrade = {}
  while True:
    printSubjMenu()
    try:
      n = int(input('Select either subject [1]..[8] or 0: '))
      if n==0:
        break
      if n not in range(1,9):
        raise ValueError('')
    except ValueError as e:
      print(f' ERROR: only interger 1..8 accepted!')
      continue
    g = input(f'Enter grade you get for [{subList[n-1]}]: ').upper()
    if g not in grade.keys():
      print(f' ERROR: either of A,B+,B,..F is accepted!')
      continue
    subGrade[subList[n-1]] = g 
    print(subGrade)
  return subGrade

def printSubjMenu():
  lenSubList, s, ss = len(subList), [], ''
  for i in range(lenSubList):
    ss = f'[{i+1}] {subList[i]}'
    s.append(f'{ss:<25}')
    if len(s)%2==0:
      print(s[0],s[1])
      s = []

def calGrade(v):
  lenV, C, myS = len(v), 0, 0 
  for s,g in v.items():
    C, myS = C + subDic[s], myS + subDic[s] * grade[g] 
    print(f'{s} ({g})', end='')
    lenV -= 1 
    if lenV==0:
      print()
    else:
      print(', ', end='')
  print(f' GPA: {myS/C:.2f}')
    
def printGrades(studDic):
  for n,v in studDic.items():
    print(f'Name: {n}')
    calGrade(v)

## main begins here
subDic = {'Physic I': 3, 'Lab Physic I': 1, 'Math I': 3, 'Com Programming': 3, 'Thai Lang Com': 3, 'Art of Living': 3, 'Land of Smile': 3, 'Intro Japanese': 3}
subList = ['Physic I', 'Lab Physic I', 'Math I', 'Com Programming', 'Thai Lang Com', 'Art of Living', 'Land of Smile', 'Intro Japanese']
grade = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}

#studDic = {'Kun Toto': {'Physic I': 'A', 'Lab Physic I': 'C+', 'Thai Lang Com': 'B+', 'Land of Smile': 'D', 'Intro Japanese': 'B+'}, 'Somchai Rukdee': {'Lab Physic I': 'B+', 'Physic I': 'B', 'Math I': 'C', 'Com Programming': 'D', 'Thai Lang Com': 'F', 'Art of Living': 'A', 'Land of Smile': 'A'}}

subjGrade = getSubGrade()
print(subjGrade)
