def commaCode(m):
  if m==[]:
    return
  if len(m)==1:
    print(m[0])
  else:
    for i in range(len(m)):
      if i==len(m)-1:
        print(f'and {m[i]}', end='')
      elif i<len(m)-1-1:
        print(f'{m[i]}, ', end='')
      else:
        print(f'{m[i]} ', end='')
    print()

m = [1,2,3,4,'Hello']
commaCode(m)
commaCode([1,'Hello World'])
commaCode([1])
commaCode([])
