def sum_price():
  print('Menu\n0. Finish\n1. Latte = 40\n2. Espresso = 45')
  print('3. Americano = 50\n4. Mocca = 55\n5. Cappuccino = 60')
  tprice = 0
  while True:
    caf = int(input('coffee : '))
    if caf==0:
      print(f'total price : {tprice}')
      return tprice
    amt = int(input('amount : '))
    if caf==1:
      tprice += 40*amt
    elif caf==2:
      tprice += 45*amt
    elif caf==3:
      tprice += 50*amt
    elif caf==4:
      tprice += 55*amt
    elif caf==5:
      tprice += 60*amt
    
def change(tprice, pay):
  change = pay - tprice
  print(f'customer\'s change : {change}')
  if change//1000 > 0:
    print(f'change 1000 : {change//1000}')
    change %= 1000
  if change//500 > 0:
    print(f'change 500 : {change//500}')
    change %= 500
  if change//100 > 0:
    print(f'change 100 : {change//100}')
    change %= 100
  if change//50 > 0:
    print(f'change 50 : {change//50}')
    change %= 50
  if change//20 > 0:
    print(f'change 20 : {change//20}')
    change %= 20  
  if change//10 > 0:
    print(f'change 10 : {change//10}')
    change %= 10
  if change//5 > 0:
    print(f'change 5 : {change//5}')
    change %= 5  
  if change > 0:
    print(f'change 1: {change}')

tprice = sum_price()
pay = int(input('customer pay : '))
change(tprice, pay)
