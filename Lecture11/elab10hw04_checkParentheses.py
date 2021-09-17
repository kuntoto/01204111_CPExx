def myPop(m): 
  ''' delete and return the last element in 
      a list if it exists'''
  if len(m)==0:
    return None, m
  else:
    res = m[len(m)-1]
    del m[len(m)-1]
    return res, m

def checkBalance(s):
  s,lpar,rpar,alist = list(s),"{([","})]",[]
  balanced = True
  for i in s:
    if i in "{([":
      alist.append(i)
      #print(alist)
    elif i in "})]":
      last,alist = myPop(alist)
      #print(f'alist:{alist},last:{last},i:{i}')
      if last==None or rpar[lpar.index(last)]!=i:
        balanced = False
        break  
  if len(alist)!=0: balanced = False
  return balanced

class py_solution:
  def __init__(self, s):
    self.s = list(s)
  def is_valid_parentheses(self):
    return checkBalance(s)

### main begins here
### test cases
#s = "{({})[[]]()}"
#s = "(\n("
#s = "((((([])))))\n{{{{{[]}}}}}"
s = input('input: ')
myStr = py_solution(s)  
if myStr.is_valid_parentheses():
  print('valid parentheses')
else:
  print('invalid parentheses')
