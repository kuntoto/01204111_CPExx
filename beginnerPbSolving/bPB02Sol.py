### [simpleCalculator] เครื่องคิดเลขอย่างง่าย
import sys

def plus(x,y):
  return x+y

def minus(x,y):
  return x-y

def mul(x,y):
  return x*y

def div(x,y):
  if y==0:
    print(f'ERROR: Division by zero not allowed!')
    sys.exit()
  return x/y

def mod(x,y):
  if y==0:
    print(f'ERROR: Division by zero not allowed!')
    sys.exit()
  return x%y

def getInputAndCal():
  x = int(input('x: '))
  op = input('Operator: ')
  y = int(input('y: '))
  if op == '+':
    print(plus(x,y))
  elif op == '-':
    print(minus(x,y))
  elif op == '*':
    print(mul(x,y))
  elif op =='%':
    print(mod(x,y))
  elif op =='/':
    print(f'{div(x,y):.2f}')
  else:
    print('Unknown Operator')

## main begins here
getInputAndCal()

### change มาคคุง เด็กพาร์ทไทม์
n = int(input())

if n//1000 > 0:
  print(f'1000 => {n//1000}')
  n%=1000
else:
  print(f'1000 => 0')

if n//500 > 0:
  print(f'500 => {n//500}')
  n%=500
else:
  print(f'500 => 0')

if n//100 > 0:
  print(f'100 => {n//100}')
  n%=100
else:
  print(f'100 => 0')

if n//50 > 0:
  print(f'50 => {n//50}')
  n%=50
else:
  print(f'50 => 0')

if n//20 > 0:
  print(f'20 => {n//20}')
  n%=20 
else:
  print(f'20 => 0')

if n//10 > 0:
  print(f'10 => {n//10}')
  n%=10
else:
  print(f'10 => 0')

if n//5 > 0:
  print(f'5 => {n//5}')
  n%=5
else:
  print(f'5 => 0')

print(f'1 => {n}')  


### [date] เมื่อไหร่เราจะได้พบกันจุ้บ<3
def isLeapYear(n):
  if n%4==0 and n%100!=0 or n%400==0:
    return True
  return False

def nbDinMonth(m, y):
  if m == 2:
    if isLeapYear(y):
      return 29
    else:
      return 28
  elif m in [4,6,9,11]:
    return 30
  else:
    return 31

d = int(input('d: '))
m = int(input('m: '))
y = int(input('y: '))

mysum = 0
for i in range(1, m):
  mysum += nbDinMonth(i,y)

mysum += d
print(mysum)

### My_grade เกรดของชั้น
def grade2nb(g):
  g = g.upper()
  if g=='A':
    return 4.0
  elif g=='B+':
    return 3.5
  elif g=='B':
    return 3.0
  elif g=='C+':
    return 2.5
  elif g=='C':
    return 2.0
  elif g=='D+':
    return 1.5
  elif g=='D':
    return 1.0
  else:
    return 0

subj = int(input('How many subject: '))
mysum, credit = 0, 0
for i in range(subj):
  c = int(input(f'Subject {i+1} Credits: '))
  g = grade2nb(input(f'Subject {i+1} Grade: '))
  mysum += c*g
  credit += c
gpa = mysum/credit
print(f'Output: Total Credit = {credit:.1f} ,GPA = {gpa:.2f}')

### dec_to_hex คอปเตอร์ยอดนักคณิตศาสตร์
def dec2hex(n):
  hexa = ''
  while n > 0:
    rem = n%16
    if rem < 10:
      hexa = str(n%16) + hexa
    elif rem == 10:
      hexa = 'A' + hexa
    elif rem == 11:
      hexa = 'B' + hexa
    elif rem == 12:
      hexa = 'C' + hexa
    elif rem == 13:
      hexa = 'D' + hexa
    elif rem == 14:
      hexa = 'E' + hexa
    else:
      hexa = 'F' + hexa
    n = n//16
  return hexa

## main begins here
while True:
  dec = int(input('Input Decimal: '))
  if dec == -1:
    break
  hexa = dec2hex(dec)
  print(f'Hex: {hexa}')
print('Good bye.')
