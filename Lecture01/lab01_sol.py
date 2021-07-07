### HELLO STUDENT
name = input('Please tell me your name : ')
print('Hello, teacher and lovely TA..')
print('My name is', name)
print(name + ' is CPE#35 student..')
print(f"{name}'s favorite is Python.")
print('THANKS')

### Shape
w = float(input('width : '))
l = float(input('length : '))
print(f'area : {w * l}')
print(f'perimeter : {2*w + 2*l}')

### Vat
sum_price = float(input('summary price : '))
food = sum_price / 1.07
vat = food * 0.07
print(f'food : {food:.2f}')
print(f'vat : {vat:.2f}')

### Energy
milk = int(input('Milk: '))
coffee = int(input('Coffee: '))
print(f'{milk*coffee**2}')

### calculate
m = int(input('Money: '))
s = int(input('Son: '))
print(f'{m//s} {m%s}')

### String Concatenation
fname = input('Enter your first name : ')
lname = input('Enter your last name : ')
print("My name is " + fname, lname)

### How long
s1 = len(input('First sentence: '))
s2 = len(input('Second sentence: '))
s3 = len(input('Third sentence: '))
print((s1+s2)*s3)

### Datatype
t = input('Input text: ')
n = float(input('Input number: '))
print(f'I can print string with another datatype like this -> {t} {n+44.112}')

### เสาไฟกินรี
h = float(input('Hight : '))
c = float(input('Cost : '))
if h > 8  and c <= 75000:
  print('NO')
elif h > 4 and c <= 30000:
  print('NO')
elif h > 1 and c <= 5000:
  print('NO')
elif c < 1000:
  print('NO')
else:
  print('YES')  

### String Replication
text = input('Enter string : ')
times = int(input('Enter number of times : '))
print(text * (times-1)) 


### เสี่ยนักซิ่ง
a = float(input('A : '))
b = float(input('B : '))
x = float(input('X : '))
r = int(3600*(x/a - x/b))
print(f'Wait : {r} sec')

### full_divide
a = int(input('Input Dividend: '))
b = int(input('Input Divider: '))
print(f'{a} = {b} * {a//b} + {a%b}')

### Age_Classification
a = int(input('Enter your age : '))
if a >= 60:
  print('You are Senior Adult.')
elif a >= 19:
  print('You are Adult.')
elif a >= 13:
  print('You are Adolescence.')
else:
  print('You are Child.')

### Datatype2
n = int(float(input('Input decimal: ')))
print((str(n)+' ')*n)

### 4_num_sort
a,b,c,d = map(int,input().split())
one,two,three,four = 0,0,0,0

# บิกินเนอร์ไม่ต้องตกใจ ป๋มทำไม่ได้เหมือนกันฮับ
