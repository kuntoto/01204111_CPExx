def collatz(number):
  if number%2==0:
    res = number//2
  else:
    res = 3*number+1
  print(res)
  return res

## main begins here
print('Enter number:')
while True:
  try:
    n = int(input())
  except ValueError:
    print('Input must only be integer, try again..')
    continue
  result = collatz(n)
  if result == 1:
    break
