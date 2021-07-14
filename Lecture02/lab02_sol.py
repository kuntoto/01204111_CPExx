### เสาไฟกินรี 2 - เสาไฟใจเกเร
nbPole = int(input('number of electric poles : '))

max1, max2 = -99998, -99999
for i in range(nbPole):
  poleCost = int(input())
  if poleCost > max1:
    max2 = max1
    max1 = poleCost
  elif poleCost > max2 or max2 == max1:
    max2 = poleCost
  #print(f'#{i+1}: max1={max1},max2={max2}')

if nbPole == 1:
  print('NO')
elif max1 > 3*max2:
  #print(f'YES\n{max1},{max2}')
  print(f'YES\n{max1}')
else:
  print('NO')
       
### How long 2
d = int(input('Input distance(kilometer): '))

m = 0
for i in range(1, d+1):
  m += 10
  if i < d and i%6 == 0:
    m += 10

h, mn = m//60, m%60
print(f'It takes {h} hours and {mn} minutes to reach the destination.')

### Catch Me
t, crimeD, polD = 1, 100, 0

while True:
  polGo = int(input('Input distance: '))
  polD += polGo
  print(f'Police distance: {polD}')
  crimeD += 2**t
  t += 1
  print(f'Criminal distance: {crimeD}')
  if polD >= crimeD:
    print('Caught him!')
    break

### ทั้งนั้นเลย
n = int(input())
for i in range(n):
  print('O'*(i+1))

### princess
ss = int(input('s: '))
h = ss//3600
s = ss - h*3600
m = s//60
se = s%60
print(f'{ss} seconds equals {h} hour(s) {m} minute(s) and {se} second(s)')

### Sale
d = int(input('How many day : '))
mysum, s = 0, 5
for i in range(d):
  p = float(input(f'Input price in day {i+1} : '))
  mysum += p*(100-s)/100
  s += 1
print(f'Summary price = {mysum:.2f}')

### Buzznaldo
m = int(input('How long have Buzz played ?: '))
h = m//60
s = m%60
if s > 20:
  h,s = h+1, 0
p = h*900
if h >= 5:
  p = p * 0.7
elif h == 4:
  p = p * 0.8
elif h >= 2:
  p = p * 0.9
print(f'Total price is {int(p)} baht.')

### bulotelli
is_injured = input('Is Bulotelli injured?(y/n) ')
if is_injured == 'y':
  print('Not available')
else:
  is_late = input('Is Bulotelli late for the training?(y/n) ')
  if is_late == 'y':
    is_well_train = input('Did Bulotelli perform well in training?(y/n) ')
    if is_well_train == 'y':
      print('Substitute')
    else:
      print('Not selected')
  else:
    print('Starter')
    
### Arrow
n = int(input())
A = input('Arrow : ')
B = input('Stick : ')

for i in range(n,0,-1):
  print(' '*i + A*(2*(n-i+1)-1))
for i in range(n):
  print(' '*n + B)

### Count_1
x = int(input())
y = int(input())
p = int(input())

c,k = x, 0
while c <= y:
  if c%p == 0:
    c += 11
    continue
  if c > y:
    break
  print(c, end=' ')
  c += 1
  k += 1
  if k%10:
    print()

### เสาไฟกินรี 3 - งบประมาณใหม่
h = int(input('hight of electric poles : '))
nbP = int(input('number of electric poles : '))
max1, max2 = -99998, -99999
total_pCost = 0
IS_KIN = False

for i in range(nbP):
  poleCost = int(input())
  if poleCost > max1:
    max2 = max1
    max1 = poleCost
  elif poleCost > max2 or max2 == max1:
    max2 = poleCost
  total_pCost += poleCost

if nbP == 1:
  aver_pCost = total_pCost
elif max1 > 3*max2:
  total_pCost -= max1
  aver_pCost = total_pCost / (nbP-1)
  aver_pCost += max1 / (max1//max2)
  IS_KIN = True
else:
  aver_pCost = total_pCost / nbP

aver_pCost = int(aver_pCost)
if not IS_KIN:  
  if h > 8 and aver_pCost > 75000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-75000}')
  elif h > 4 and aver_pCost > 30000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-30000}')
  elif h > 1 and aver_pCost > 5000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-5000}')
  elif h == 1 and aver_pCost > 1000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-1000}')
  else:
    print(f'Avg: {aver_pCost}\nNO')
else:
  if h > 8 and aver_pCost > 100000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-100000}')
  elif h > 4 and aver_pCost > 50000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-50000}')
  elif h > 1 and aver_pCost > 10000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-10000}')
  elif h == 1 and aver_pCost > 3000:
    print(f'Avg: {aver_pCost}\nYES {aver_pCost-3000}')
  else:
    print(f'Avg: {aver_pCost}\nNO')

### date
def isLeap(y):
  if y%4==0 and (y%100!=0 or y%400==0):
    return True
  else:
    return False

d = int(input('d: '))
m = int(input('m: '))
y = int(input('y: '))

mysum = 0

for month in range (1, m):
  if month == 2:
    if isLeap(y):
      mysum += 29
    else:
      mysum += 28
  elif month in [1,3,5,7,8,10,12]:
    mysum += 31
  else:
    mysum += 30

mysum += d

print(mysum)
      
### [any max consec] นับเลขให้หนูหน่อยสิ  NOT YET DEBUGGGGG
myMax = -99999
maxC = 0
myMax2, maxC2 = myMax, maxC

while True:
  n = int(input())
  if n == 0:
    break
  if n > myMax:
    maxC = 1
    myMax = n
    if myMax >= myMax2 and maxC > maxC2:
      myMax2,maxC2 = myMax, maxC
  elif n == myMax:
    maxC += 1
    if myMax >= myMax2 and maxC > maxC2:
      myMax2,maxC2 = myMax, maxC
  print(myMax,maxC,myMax2,maxC2)

print(f'{maxC2}\n{myMax2}')

### [any max consec] นับเลขให้หนูหน่อยสิ
myMax = -99999
maxC = 0
myMax2, maxC2 = myMax, maxC

while True:
  n = int(input())
  if n == 0:
    break
  if n != myMax2:
    myMax2 = n
    maxC2 = 1
  elif n == myMax2:
    maxC2 = maxC2 + 1
  if maxC2 > maxC:
    myMax = myMax2
    maxC = maxC2

if maxC > 0:
  print(f'{maxC}\n{myMax}')

### O ทั้งนั้นเลย 2
n = int(input())

for i in range(1, n+1, 2):
  print(' '*((n-i)//2), end='')
  print('O'*i)

### O ทั้งนั้นเลย 3
n = int(input())

for i in range(1, n+1, 2):
  print(' '*((n-i)//2), end='')
  print('O'*i)
for i in range(n-2, 0, -2):
  print(' '*((n-i)//2), end='')
  print('O'*i)

### [Hell Factory] โรงงานนรก
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

round = 0
while True:
  if a>=b and b>=c:
    a -= 1; b-=1; c+=1
  elif a>=c and c>=b:
    a -= 1; c-=1; b+=1  
  elif b>=a and a>=c:
    b -=1; a-=1; c+=1  
  elif b>=c and c>=a:
    b -=1; c-=1; a+=1
  elif c>=a and a>=b:
    c-=1; a-=1; b+=1
  elif c>=b and b>=a:
    c-=1; b-=1; a+=1
  round += 1
  #print(f'#{round}: a={a} b={b} c={c}')
  if a+b+c == 1:
    break

if a==1:
  print('A')
elif b==1:
  print('B')
else:
  print('C')
