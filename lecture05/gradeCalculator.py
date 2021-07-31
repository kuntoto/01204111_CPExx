def displaySubjectMenu():
  c, s, ss = 1, '', []
  for k,v in subDic.items():
    s += f'[{c}] {k} '
    if subDic[k] == 1:
      s += f'(1 credit)'
    else:
      s += f'({subDic[k]} credits)'
    ss.append(s)
    s, c = '', c+1  
    if c%2 == 1:
      #print(ss)   
      print(f'{ss[0]:<30}{ss[1]}')
      ss = []
  print(f'[{c}] print GPA')

def calGPA(enrollSub):
  mysum, credit = 0, 0
  for k,v in enrollSub.items():
    mysum += subDic[k] * grade[v]
    credit += subDic[k]
  gpa = f'{mysum/credit:.2f}'
  return gpa

def getSubjectGrade(name):
  enrollSub = {}
  while True:
    displaySubjectMenu()
    try:
      n = int(input(' Enter subject 1..8 or 9: '))
    except ValueError:
      print('ERROR: only numeric input is allowed!')
      continue
    if n == 9:
      if len(enrollSub) > 0:
        break
      else:
        print('ERROR: no subject and grade entered yet!')
        continue
    elif n >= 1 and n<=8:
      subj = subList[n-1]
      if subj in enrollSub.keys():
        print(f'WARNING: Subject [{subj}] already been registered!')
        continue
      g = input(' Your grade: ').upper()
      if g not in grade.keys():
        print('ERROR: only either grade A,B+,B,..,D,F is allowed!')
        continue
      enrollSub[subj] = g
      print(name, enrollSub)
    else:
      print('ERROR: only 1..9 is allowed!')
  return enrollSub

def getStudGrade():
  studDic = {}
  while True:
    name = input('Enter student\'s name: ')
    if name == '':
      print('>> You want to print all students\' grades..')
      break
    enrollSub = getSubjectGrade(name)
    print(enrollSub)
    gpa = calGPA(enrollSub)
    print(f'{name}\'s GPA: {gpa}')
    studDic[name] = enrollSub
  return studDic

def test_getSubjectGrade_calGPA():
  enrollSub = getSubjectGrade()
  print(enrollSub)
  gpa = calGPA(enrollSub)
  print(f'GPA: {gpa}')

def printGrades(studDic):
  s = ''
  for k,v in studDic.items():
    s+= f'{k}: '  # name
    for p,q in v.items():  # enrolled subject and grade
      s += f'{p} ({subDic[p]}c,{q}), '
    s += f'GPA={str(calGPA(v))}'  
    print(s)
    s = ''
  print('DONE GoodBye..')

def test_printGrades():
  studDic = {'Kun Toto': {'Physic I': 'A', 'Lab Physic I': 'C+', 'Thai Lang Com': 'B+', 'Land of Smile': 'D', 'Intro Japanese': 'B+'}, 'Somchai Rukdee': {'Lab Physic I': 'B+', 'Physic I': 'B', 'Math I': 'C', 'Com Programming': 'D', 'Thai Lang Com': 'F', 'Art of Living': 'A', 'Land of Smile': 'A'}}
  printGrades(studDic)

## main begins here
subDic = {'Physic I': 3, 'Lab Physic I': 1, 'Math I': 3, 'Com Programming': 3, 'Thai Lang Com': 3, 'Art of Living': 3, 'Land of Smile': 3, 'Intro Japanese': 3}
subList = ['Physic I', 'Lab Physic I', 'Math I', 'Com Programming', 'Thai Lang Com', 'Art of Living', 'Land of Smile', 'Intro Japanese']
grade = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}

studDic = getStudGrade()
printGrades(studDic)
