### ยอดนักคำนวน 2 [Great Mathematicians 2]
def Nplus(n):
  global N
  N+=n

def Nminus(n):
  global N
  N-=n

def Ntimes(n):
  global N
  N*=n

def Ndivided(n):
  global N
  N/=n

N = 10
Nplus(5)
Nminus(3)
Ntimes(6)
Ndivided(3)
print(f'{N:.0f}')

c = input()
if c == '1':
    Nplus(12)
    print(f'{N:.0f}')
if c == '2':
    Nminus(6)
    print(f'{N:.0f}')
if c == '3':
    Ntimes(2)
    print(f'{N:.0f}')
if c == '4':
    Ndivided(6)
    print(f'{N:.0f}')

### เสี่ยโออยากไปเที่ยวจัง

def getInput():
  n = int(input('N = '))
  res = []
  for i in range(1,n+1):
    k = int(input(f'cost of day {i} = '))
    res.append(k)
  return res

def getMinCost(res):
  if len(res) <= 3:
    return sum(res)
  last = len(res)-3+1
  minC = 99999999
  for i in range(last):
    tmp = res[i] + res[i+1] + res[i+2]
    #tmp = sum(res[i:i+3])
    if tmp < minC:
      minC = tmp
  return minC

res = getInput()
minC = getMinCost(res)
print(f'Min cost of 3 days = {minC}')

### Basic_list
from statistics import median
n, a = 0, []

while n < 5:
  k = int(input('Enter a positive number: '))
  if k <= 0:
    continue
  n += 1
  a.append(k)

#print(a)
print(f'sum: {sum(a)}')
print(f'min: {min(a)}')
print(f'max: {max(a)}')
print(f'med: {median(a)}')

### Hacker คอปเตอร์คุงยอดนักแฮก

s = input()
c = 0
while True:
  k = input()
  if k != s[c]:
    print('Fail!!')
    break
  c += 1
  if c == 3:
    print('Succeed!!')
    break

### [stairs] บันไดตัวอักษร
def draw(m):
  for i in range(1, len(m)+1):
    print(str(m[i-1])*i)

while True:
  s = input().split()
  if s != ['0']:
    draw(s)
  else:
    print('Good Bye.')
    break

### [LOVE NOTE 1] สมุดโน้ตกระชากใจ 1
def lovenote(s):
  for i in range(len(s)):
    for j in range(len(s)):
      if i==j:
        print(s[j].upper(), end='')
      else:
        print(s[j], end='')
    print()

s = input('Input name: ')
lovenote(s)

### [LOVE NOTE 2] สมุดโน้ตกระชากใจ 2
def ln(s, i):
  res = ''
  for j in range(len(s)):
    if j==i:
      res += s[j].upper()
    else:
      res += s[j]
  return res

def lovenote(s):
  for i in range(len(s)):
    print(ln(s, i), ln(s[::-1], i))

s = input('Input name: ')
lovenote(s)

### Add & Remove
def getListInput():
  s = input()
  res = s.split()
  return res

m = getListInput()
while True:
  cmd, attr = getListInput()
  cmd, attr = cmd.upper(), int(attr)
  if cmd == 'A':
    m.append(attr)
  elif cmd == 'S' and attr < len(m):
    print(m[attr])
  elif cmd == 'R':
    m = m.pop(attr)
  elif cmd == 'E':
    if len(m) > 0:
      for i in range(len(m)):
        print(m[i], end=' ')
      print()
    break

### R U Lucky?

nb = list(input())
nb = [int(i) for i in nb]

if nb[1] == 8:
  if sum(nb) < 56 and sum(nb)%13==0:
    print('Have bad luck.')
  else:
    print('Have good luck.')
else:
  BADLUCK = False
  for i in range(len(nb)-1):
    if str(nb[i]) + str(nb[i+1]) in ['20', '13', '18', '80', '31', '93']:
      print('Have bad luck.')
      BADLUCK = True
      break
  if not BADLUCK:
    print('Have good luck.')

### Ching Chok
def getInput():
  lnb = input('Enter lucky number : ')
  n = int(input('Enter amount of candidates : '))
  ids = []
  for i in range(1, n+1):
    tmp = input(f'Enter ID card number {i}: ')
    ids.append(tmp)
  return lnb, ids

def countLnb(s, nb):
  res = 0
  for i in range(len(s)):
    if s[i]==nb:
      res += 1
  return res

def run():
  lnb, ids = getInput()
  #print(lnb, ids)
  lnbCount = []
  for n in ids:
    lnbCount.append(countLnb(n, lnb))
  #print(ids)
  #print(lnbCount)
  maxC = max(lnbCount)
  res = []
  for i in range(len(ids)):
    if lnbCount[i] == maxC:
      res.append(ids[i])
  #print(res)
  res = [int(x) for x in res]
  #print(res)
  print('Winner:', max(res))

run()

### isPrime
def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  for i in range(2, n):
    if n%i==0:
      return False
  return True

def test_isPrime():
  for i in range(102):
    if isPrime(i):
      print(i, end=' ')
  print()

def run():
  res = []
  while True:
    n = int(input())
    if n==0:
      break
    if isPrime(n):
      res.append(n)
  if len(res) > 0:
    for i in range(len(res)):
      if (i+1)%11==0:
        print()
      print(res[i], end=' ')

run()

### [twin prime] ฉันต้องคู่กับเธอมีเพียงแต่เธอคนเดียวเท่านั้น
def isPrime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  for i in range(2, n):
    if n%i==0:
      return False
  return True

n = int(input("N: "))
while n < 99999:
  if isPrime(n) and isPrime(n+2):
    print((n, n+2))
    break
  n += 1
