## Savings Account
def calAmount(a, r, y):
  res = a * (1+r/100)**y
  return res

a = float(input('Enter initial amount in Baht: '))
r = float(input('Enter interest rate in percent: '))

print(f'Total amount after 1 year is {calAmount(a,r,1):.2f} Baht.')
print(f'Total amount after 5 year is {calAmount(a,r,5):.2f} Baht.')
print(f'Total amount after 10 year is {calAmount(a,r,10):.2f} Baht.')
print(f'Total amount after 20 year is {calAmount(a,r,20):.2f} Baht.')

## Trapezoid
def trapezoid(a,b,h):
  res = (a+b)/2*h
  return res

print('Specify your trapezoid\'s properties.')
a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
h = float(input('Enter height: '))
print(f'The trapezoid area is {trapezoid(a,b,h):.2f}')

## Electric Applicance Store
def calPrice(tv,dvd,aud):
  total = tv*7200 + dvd*1800 + aud*3600
  print(f'Total price is {total:.2f} baht.')
  if total >= 24000:
    discount = total * 0.2
    print(f'Discount: {discount:.2f} baht.')
    total -= discount
  print(f'Please pay {total:.2f} baht. Thank you very much.')

tv = int(input('How many TVs to buy? '))
dvd = int(input('How many DVD players to buy? '))
aud = int(input('How many audio systems to buy? '))
calPrice(tv,dvd,aud)

## Quadratic Equation Solver
import sys
from math import sqrt

a = float(input('Value of 1st coefficient: '))
if a==0:
  print("1st coefficient can't be zero. Program exits.")
  sys.exit()

b = float(input('Value of 2nd coefficient: '))
c = float(input('Value of 3rd coefficient: '))

d = b**2 - 4*a*c
if d==0:
  r = -b/2/a
  print(f'One real root: {r:.3f}')
elif d>0:
  r1 = (-b+sqrt(d))/2/a
  r2 = (-b-sqrt(d))/2/a
  print(f'There are two real roots: {r1:.3f} and {r2:.3f}')
else:
  r = -b/2/a
  i = sqrt(-1*d)/2/a
  if i > 0:
    print(f'There are two complex roots: {r:.3f}+{i:.3f}i and {r:.3f}-{i:.3f}i')
  else:
    print(f'There are two complex roots: {r:.3f}+{-1*i:.3f}i and {r:.3f}-{-1*i:.3f}i')

## Final Grade
def getInput():
  hw = int(input('What is the percentage for homework? '))
  mt = int(input('What is the percentage for midterm? '))
  fn = int(input('What is the percentage for final? '))
  return hw,mt,fn

def calGrade(sc):
  grade = ''
  if sc >= 80:
    grade = 'A'
  elif sc >= 75:
    grade = 'B+'
  elif sc >= 70:
    grade = 'B'
  elif sc >= 65:
    grade = 'C+'
  elif sc >= 60:
    grade = 'C'
  elif sc >= 55:
    grade = 'D+'
  elif sc >= 50:
    grade = 'D'
  else:
    grade = 'F'
  return grade

hw, mt, fn = getInput()
score = hw*.15 + mt*.40 + fn*.45
grade = calGrade(score)
print(f'Total score: {score:.2f}')
print(f'Your grade is {grade}')

### Diagonal Banner
s = input('Input a string: ')
slen = len(s)
for i in range(slen):
  print(' '*i + s[i])

### print_triangle
def pat1(c, n):
  for i in range(n):
    print(c*(i+1))

def pat2(c, n):
  for i in range(n,0,-1):
    print(c*(i))

def pat3(c, n):
  for i in range(n):
    print(' '*(n-i-1) + c*(i+1))

def pat4(c, n):
  for i in range(n-1,-1,-1):
    print(' '*(n-i-1) + c*(i+1))

p = int(input('pattern: '))
c = input('char: ')
n = int(input('n: '))
if p==1:
  pat1(c,n)
elif p==2:
  pat2(c,n)
elif p==3:
  pat3(c,n)
elif p==4:
  pat4(c,n)

### Sum of Numbers
sum1,sum2 = 0,0
while True:
  n = float(input('Enter a number (or 0 to exit): '))
  if n == 0:
    break
  if n > 0:
    sum1 += n
  else:
    sum2 += n

print(f'Sum of positive numbers is {sum1:.2f}')    
print(f'Sum of negative numbers is {sum2:.2f}') 

### Frog and Well
import sys

h = int(input('Enter the depth of the well: ')) 
u = int(input('How high the frog can jump up? ')) 
d = int(input('How far the frog slips down? ')) 

if h>u and d>=u:
  print('The frog will never escape from the well.')
  sys.exit()

frog_depth = h
day = 0
while frog_depth > 0:
  day += 1
  frog_depth -= u
  if frog_depth <= 0:
    break
  print(f'On day {day} the frog leaps to the depth of {frog_depth} meters.')
  frog_depth += d
  print(f'At night he slips down to the depth of {frog_depth} meters.')

print(f'Frog is free on day {day}.')
