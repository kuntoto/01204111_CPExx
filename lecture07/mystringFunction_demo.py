def upper(s):
  """upper(s): convert all character in string s to uppercase"""
  res = ''
  for i in s:
    if i >= 'a' and i <= 'z':
      res += chr(ord('A') + (ord(i)-ord('a')))
    else:
      res += i
  return res

def isupper(s):
  if len(s)==0:
    return False
  res = False
  for i in s:
    if i >= 'a' and i <= 'z':
      res = False
      break
    elif i >= 'A' and i <= 'Z':
      res = True
  return res

def lower(s):
  """lower(s): convert all character in string s to lowercase"""
  res = ''
  for i in s:
    if i >= 'A' and i <= 'Z':
      res += chr(ord('a') + (ord(i)-ord('A')))
    else:
      res += i
  return res

def islower(s): # NOT IMPLEMENTED YET 
    return True
    
def isalpha(s):
  if len(s)==0:
    return False
  res = True
  for i in s:
    if not(lower(i)>='a' and lower(i)<='z'):
      res = False
      break
  return res

def isalnum(s):
  if len(s)==0:
    return False
  res = True
  for i in s:
    if not((lower(i)>='a' and lower(i)<='z') or (i>='0' and i<='9')):
      res = False
      break
  return res

def isdecimal(s):
  if len(s)==0:
    return False
  res = True
  for i in s:
    if not(i>='0' and i<='9'):
      res = False
      break
  return res

def startswith(s, q):
  """startswith(s, q): return True if string s starts with string q"""
  lenS, lenQ = len(s), len(q)
  if lenQ==0:
    return True
  elif lenS==lenQ and s==q:
    return True
  elif lenQ > lenS:
    return False
  else:
    res = True
    for i in range(0, lenQ):
      if s[i]!=q[i]:
        return False 
  return True

def endswith(s, q): # NOT IMPLEMENTED YET
    return True

def join(s, mylist):
  '''join(s,mylist): join each list element with string s'''
  res = ''
  for i in range(len(mylist)):
    if i==len(mylist)-1:
      res += mylist[i]
    else:
      res += mylist[i] + s
  return res

def partition(s, sep):
  """partition(s, sep): return a list of strings that look like s.partition(sep)"""
  # base case
  if s==None:
    return []
  if sep=='':
    print('ERROR: empty seperator is not allowed.')
    return None
  if not sep in s:
    return [s]
  # normal case  
  #n = find(s, sep) # <-- NOT IMPLEMENTED YET
  n = s.find(sep)
  if n==-1:
    return [s]
  front = s[:n]
  back = s[n+len(sep):]
  return tuple([front] + [sep] + [back])
  
def test_case1():
  global s
  print(lower(s))
  print(upper(s))
  print('---islower')
  print(islower('asd fgh 64#\n '), islower('asd fgh 64#\n Q '), islower(' '), islower(''), islower('!@#$%^&*()_+'), islower('!@#$%^&*()_+a'))
  print('asd fgh 64#\n '.islower(), 'asd fgh 64#\n Q '.islower(), ' '.islower(), ''.islower(), '!@#$%^&*()_+'.islower(), '!@#$%^&*()_+a'.islower())
  print('---isupper')
  print(isupper('ASD FGH 64#\n '), isupper('ASD FGH 64#\n q '), isupper(' '), isupper(''), isupper('!@#$%^&*()_+'), isupper('!@#$%^&*()_+A'))
  print('ASD FGH 64#\n '.isupper(), 'ASD FGH 64#\n q '.isupper(), ' '.isupper(), ''.isupper(), '!@#$%^&*()_+'.isupper(), '!@#$%^&*()_+A'.isupper())
  print('---isalpha()')
  print(isalpha('asdfQWE'), isalpha('a1'), isalpha(''), isalpha(' A'), isalpha('1#'))
  print('asdfQWE'.isalpha(), 'a1'.isalpha(), ''.isalpha(), ' A'.isalpha(), '1#'.isalpha())
  print('---isalnum')
  print(isalnum('123a'), isalnum('Asd'), isalnum('123a@'), isalnum(''), isalnum('a123\n'))
  print('123a'.isalnum(), 'Asd'.isalnum(), '123a@'.isalnum(), ''.isalnum(), 'a123\n'.isalnum())
  print('---isdecimal')
  print(isdecimal('123'), isdecimal('12 3'), isdecimal(''))
  print('123'.isdecimal(), '12 3'.isdecimal(), ''.isdecimal())
  print('---startswith')
  print(startswith(s, ''), startswith(s, 'He'), startswith(s, s+''), startswith(s, s+' '), startswith(s, 'e'))
  print('---endswith')
  print(endswith(s, ''), endswith(s, '@ku'), endswith(s, '@KU'), endswith(s, s), endswith(s, s+'@KU'))

def test_case2():
  #print('---find')
  #print(find(s, ''), find(s, 'el'), find(s, 'elll'), find(s, '@KU'))
  print('---split')
  print(split(s, ''), split(s, 'z'), split(s, ' '), sep='/')
  spam = '''Hello, world
Welcome to 111 @KU
Hope you enjoy your day?
Sincerely yours,
K.Toto
'''
  print(spam.split())
  print(split(spam, '\n'))
  print(join(', ', ['cats', 'rats', 'bats']), join('ABC', ['My','name','is','Toto.']), join('',['a','b','','d']),sep='/')
  print('---split')
  print(partition(s, '@'), partition(s,' '), sep='/')
  print(partition(s, 'KU'), sep='/')

def test_case3():
  print('---rjust, ljust, center')
  s = 'Hello'
  print(f"'{rjust(s,10)}'", f"'{ljust(s,10)}'", f"'{center(s,6)}'", sep="/")

def myminus(x=1, y=2):
    return x-y

def test_myminus():
    print(f'myminus(2,1)={myminus(2,1)}', f'myminus(2)={myminus(2)}', f'myminus(y=2,x=1)={myminus(y=2,x=1)}', sep=' / ')
    print(f'myminus()={myminus()}', f'myminus(y=-2)={myminus(y=-2)}', f'myminus(y=-2,x=-1)={myminus(y=-2,x=-1)}', sep=' / ')

## main begins here
s = 'Hello, welcome to 01204111 @KU'
print(s)
test_case1()
test_myminus()
