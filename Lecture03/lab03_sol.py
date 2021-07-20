### ฉันอยู่ที่นี่ [I'm here]
def AmHere(namee):
  print('Hello !!!')
  print(f'I\'m here {namee}!!!')

namee = input('Who are you going to call : ')
AmHere(namee)

### กินรีอยากออกอะไรก็ได้ 1
import math

n = int(input('How many Pi : '))
for i in range(n):
  print(math.pi)

### กินรีอยากออกอะไรก็ได้ 2
import math

n = int(input('log2 of : '))
print(math.ceil(math.log(n, 2)))

### กินรีอยากออกอะไรก็ได้ 3
import math

d = int(input('Degree : '))
print(f'sin : {math.sin(math.pi*d/180):.2f}')
print(f'cos : {math.cos(math.pi*d/180):.2f}')
print(f'tan : {math.sin(math.pi*d/180)/math.cos(math.pi*d/180):.2f}')

### กินรีอยากออกอะไรก็ได้ 4
s = input('Enter string : ')

print(f'align --- {s:>20} --- right')
print(f'align --- {s:<20} --- left')
print(f'align --- {s:^20} --- center')

### กินรีอยากออกอะไรก็ได้ 5
s = input('Dak fung : ')

if 'i know i\'m bad' in s:
  print('Find!!!')
else:
  print('Not Find...')

### เสาไฟกินรี 4 - น็อตบลูทูธ
s = input()

s = s.upper()
if s[0] == s[len(s)-1]:
  print(f'YES\n{s[0]}')
else:
  print('NO')

### [Contractor] ผู้รับเหมาก่อสร้าง
pi = 3.141592653589793

def inputShape():
  return int(input('Input Shape: '))

def calculateSphere():
  r = int(input('Input radius(meter): '))
  v = (4/3) * pi * r**3
  print(f'The volume is {v:.2f} cubic meter.')
  return v

def calculateCone():
  r = int(input('Input radius(meter): '))
  h = int(input('Input height(meter): '))
  v = pi * r**2 * h/3
  print(f'The volume is {v:.2f} cubic meter.')
  return v

def calculateCylinder():
  r = int(input('Input radius(meter): '))
  h = int(input('Input height(meter): '))
  v = pi * r**2 * h
  print(f'The volume is {v:.2f} cubic meter.')
  return v

def calculatePrism():
  w = int(input('Input width(meter): '))
  l = int(input('Input length(meter): '))
  h = int(input('Input height(meter): '))
  v = w * l * h
  print(f'The volume is {v:.2f} cubic meter.')
  return v

def calculatePyramid():
  w = int(input('Input width(meter): '))
  l = int(input('Input length(meter): '))
  h = int(input('Input height(meter): '))
  v = w * l * h / 3.
  print(f'The volume is {v:.2f} cubic meter.')
  return v

def calculatePrice(v):
  p = int(input('Price(Bath) per 1 cubic meter: '))
  price = p * v
  print(f'The price is {price:.2f} Baht.')

shape = inputShape()
if shape == 1:
  v = calculateSphere()
elif shape == 2:
  v = calculateCone()
elif shape == 3:
  v = calculateCylinder()
elif shape == 4:
  v = calculatePrism() 
elif shape == 5:
  v = calculatePyramid()    

calculatePrice(v)

### [Stickman]
def Head(n):
  print(' ', end='')
  for i in range(n):
    print('o', end='')
  print()
  for i in range(0, n, 2):
    if i > 0:
      print(' ', end='')
      print('o' +' '*(n-2) + 'o')
  print(' ', end='')
  for i in range(n):
    print('o', end='')
  print()

def Body(n):
  j = 0
  for i in range(0, n, 2):
    if i > 0:
      print(' '*(n//2) + '||')
  print('-'*(n//2) + '||' + '-'*(n//2))
  j = 0
  for i in range(0, n, 2):
    if i > 0:
      print(' '*(n//2) + '||')

def Leg(n):
  for i in range(n, 0, -2):
    print(' '*(i//2) + '/', end='') 
    print(' '*(n-i) + '\\') 

n = int(input())
Head(n)
Body(n)
Leg(n)

### Square_Sun
def Body(n):
  print(' '*(n-1) + '*'*n)
  for i in range(2,n):
    print(' '*(n-1) + '*' + ' '*(n-2) + '*')
  print(' '*(n-1) + '*'*n)

def Tail(n):
  for i in range(1,n):
    print(' '*(n-i-1) + '*', end='')
    print(' '*(n+2*(i-1)) + '*')

def Head(n):
  for i in range(n-1,0, -1):
    print(' '*(n-i-1) + '*', end='')
    print(' '*(n+2*(i-1)) + '*')

def draw(n):
  Head(n)
  Body(n)
  Tail(n)

n = int(input())
draw(n)

### ยอดนักคำนวน [Great Mathematicians]
def even_check(n):
  if n%2 == 0:
    return True
  return False

def prime_check(n):
  if n<2:
    return False
  if n==2:
    return True
  for i in range(2,n,1):
    if n%i == 0:
      return False
  return True

n = int(input('Number : '))
if not even_check(n):
  print('The number is odd')
else:
  print('The number is even')
if prime_check(n):
  print('The number is prime')
else:
  print('The number is not prime')

### [uConverter]
def checkBase(any, n):
  n = int(n)
  any = str(any).upper()
  len_any = len(any)
  if n < 2 or n > 16:
    print(f' ERROR: {n} should be in  [2, 16]!')
    return False
  global base
  base = base[:n]
  for i in range(len_any):
    if not any[i] in base:
      print(f' ERROR: {any} cannot be base [{n}]!')
      return False
  return True

def anytoten(any, n):
  any = str(any).upper()
  len_any = len(any)
  n = int(n)
  res = 0
  global base
  if checkBase(any, n):
    for i in range(len_any):
      #print(f'{any[len_any-i-1]} ', end='')
      val = base.index(any[len_any-i-1])
      #print(f'{val} x {n**i}')
      res += val * n**i
  else:
    print('ERROR from the above mentioned!!')
    return 0
  return res

base = '0123456789ABCDEF'
s = '9fda'
res = anytoten(s, '16')
print(res)

### UAENA 1 : ยูแอนา 1
def What(s):
  photo, album = True, True
  ## check whether photo
  for i in range(len(s)):
    if s[i] >= 'A' and s[i] <= 'Z':
      continue
    else:
      photo = False
      break
  if photo:
    return 'Photobook'
  else:
    ## check whether album
    for i in range(len(s)):
      if s[i] >= 'a' and s[i] <= 'z':
        continue
      else:
        album = False
        break
  if album:
    return 'Album'
  else:
    return None

def SStatus():
  global goods # adjust your global variable here
  return What(goods)

def RReal(goods):
  first, last = goods[0].upper(), goods[len(goods)-1].upper()
  if first == 'Z' and last == 'A' or (first == chr(ord(last)-1)):
    return True
  else:
    return False

def getInput():
  global goods
  goods = input('Enter merchadise code: ')
  print(SStatus())
  print(RReal(goods))

goods = ''
getInput()

### โต๊ะจีนพรรคนี้นอนน้อย [China table]

def split_str(s):
  a, b = s.split()
  return a, b

def plus(total, value):
  return total+value

def minus(total, value):
  return total-value

def getInput():
  mysum = 0
  n = int(input('How many food you have : '))
  for i in range(n):
    v, f = split_str(input())
    v, f = int(v), int(f)
    if f==1:
      mysum = plus(mysum, v)
    else:
      mysum = minus(mysum, v)  
  print(mysum)

getInput()

## [Pascal_Reverse]
def pLine(line): 
  '''https://www.geeksforgeeks.org/pascal-triangle/'''
  C = 1
  for i in range(1, line+1):
    print(C, end=' ')
    C = int(C * (line-i)/i)
  print()

def pascal(n):
  for line in range(1,n+1):
    pLine(line)

def pascalR(n):
  for line in range(n,0,-1):
    pLine(line)

n = int(input())
pascalR(n)
