import sys

def user_input():
  usd_thb_rate = float(input('Input exchange rate: '))
  if usd_thb_rate <= 0:
    print('Your exchange rate input is error.')
  else:
    usd = int(input('Input USD: '))
    if usd >= 0 and usd%5 == 0:  
      return usd_thb_rate, usd
    else:
      print('Your USD input is error.')
  sys.exit()

def user_input2(): ## no sys.exit() required
  usd_thb_rate = float(input('Input exchange rate: '))
  if usd_thb_rate > 0:
    usd = int(input('Input USD: '))
    if usd >= 0 and usd%5 == 0:
      return usd_thb_rate, usd
    else:
      print('Your USD input is error.')
  else:
    print('Your exchange rate input is error.')
  return 0,0
  
def usd_to_thb(usd, usd_thb_rate):
  thb = usd * usd_thb_rate
  return thb

def cal_commission(thb):
    #commission = thb * 0.01/100
    commission = thb * 0.01
    rem = (thb - commission) % 5
    #print(commission, rem)
    commission = commission + rem
    return commission

def cal_money_change(thb):
    b1000,b500,b100,b50,b20,b10,b5 = 0,0,0,0,0,0,0
    b1000 = int(thb // 1000)
    thb = thb % 1000
    b500 = int(thb // 500)
    thb = thb % 500
    b100 = int(thb // 100)
    thb = thb % 100
    b50 = int(thb // 50)
    thb = thb % 50
    b20 = int(thb // 20)
    thb = thb % 20
    b10 = int(thb // 10)
    thb = thb % 10
    b5 = int(thb // 5)
    return b1000,b500,b100,b50,b20,b10,b5

def exchange(usd, usd_thb_rate):
  #print(usd_thb_rate, usd)
  thb = usd_to_thb(usd, usd_thb_rate)
  #print(thb)
  commission = cal_commission(thb)
  #print(commission)
  thb = thb - commission
  print(f'You got: {thb:.2f} Thai Baht for: {usd:.2f} USD')
  b1000,b500,b100,b50,b20,b10,b5 = cal_money_change(thb)
  #print(b1000,b500,b100,b50,b20,b10,b5)
  print('Your money are')
  print(f'1000 => {b1000}')
  print(f'500 => {b500}')
  print(f'100 => {b100}')
  print(f'b50 => {b50}')
  print(f'b20 => {b20}')
  print(f'b10 => {b10}')
  print(f'b5 => {b5}')
  print(f'Exchange commission is {commission:.2f} Thai Baht')

### main begins here
#usd_thb_rate,usd = user_input()
usd_thb_rate,usd = user_input2() # no sys.exit() needed!!
if not(usd_thb_rate==0 and usd==0):
  exchange(usd, usd_thb_rate)

