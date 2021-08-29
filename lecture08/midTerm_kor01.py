def print_menu():
  s = """Coffee Menu
0. Finish
1. Latte = 40
2. Espresso = 45
3. Americano = 50
4. Mocca = 55
5. Cappuccino = 60"""
  print(s)
  
def order_coffee():
  orderedCof, total_price = {}, 0 
  print_menu()
  while True:
    m = int(input('Coffee type: '))
    if m == 0:
      print(f'Total price: {total_price}')
      break
    a = int(input(f'Amount of {cofType[m-1]}: '))
    if cofType[m-1] not in orderedCof.keys():
      orderedCof[cofType[m-1]] = a 
    else:
      orderedCof[cofType[m-1]] += a
    total_price += a * cofPrice[cofType[m-1]]
  return orderedCof, total_price
  
def change(total_price, pay):
  note = [1000,500,100,50,20,10,5,1]
  ch = pay - total_price
  print(f'Customer\'s change: {ch}')
  for n in note:
    if ch >= n:
      print(f'Change {n}: {ch//n}')
      ch %= n 
  
def print_receipt(orderedCof, name, total_price):
  print('--------- receipt ---------\nCPE35 COFFEE SHOP')
  print(f'Customer name: {name}')
  lenC = len(orderedCof)
  for c,n in orderedCof.items():
    print(f'{c} {n}', end='')
    lenC -= 1
    if lenC == 0:
      print(f', {total_price} baht')
    else:
      print(f', ', end='')
  print('Thank you\n---------------------------')

def print_report(sales_dict):
  total_price = 0
  print('---- Daily Sale Report ----')
  for name,v in sales_dict.items():
    print(f'{name} {v} baht')
    total_price += v 
  print(f'Total sale: {total_price} baht')
  print('---------------------------')

### main begins here
cofType = ['Latte', 'Expresso', 'Americano', 'Mocca', 'Cappuccino']
cofPrice = {'Latte':40, 'Expresso':45, 'Americano':50, 'Mocca':55, 'Cappuccino':60}

#orderedCof, total_price = order_coffee()
#print(orderedCof, total_price)
#change(450, 1001)
#print_receipt({'Latte':3, 'Mocca':1}, 'KunToto', 175)
#sales_dict = {"Vichaiyut": 20450, "ORARARA": 250}
#print_report(sales_dict)

sales_dict = {}
while True:
  print_menu()
  name = input('Customer name: ')
  if name == 'end day':
    print_report(sales_dict)
    break
  orderedCof, total_price = order_coffee()
  pay = int(input('Customer pay: '))
  change(total_price, pay)
  print_receipt(orderedCof, name, total_price)
  if name in sales_dict.keys():
    sales_dict[name] += total_price
  else:
    sales_dict[name] = total_price