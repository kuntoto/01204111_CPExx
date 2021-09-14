class Car:
  def __init__(self, license, brand, color):
    self.license = license
    self.brand = brand
    self.color = color
    self.report = []
  
  def __str__(self):
    return f'{self.license} - {self.color}, {self.brand}'

  def __lt__(self, rhs):
    return self.license < rhs.license

  def add_report(self, new_report):
    self.report.append(new_report)

  def print_report(self):
    for r in self.report:
      print(f'Date: {r[0]}, '+f'Maintenance: {r[1]}, '+f'Cost: {r[2]}')
    totalPay = self.total_payment()
    print(f'Total maintenance payment: {totalPay}')

  def total_payment(self):
    mySum = 0
    for r in self.report:
      mySum += float(r[2])
    return mySum

  def max_payment(self):
    myMax = -999
    for r in self.report:
      if float(r[2]) > myMax:
        myMax = float(r[2])
    print('Max maintenance payment for ' + self.__str__())
    if myMax != -999:
      for r in self.report:
        if float(r[2])==myMax:
          print(f'Date: {r[0]}, '+f'Maintenance: {r[1]}, '+f'Cost: {r[2]}')
    else:
      print(' No maintenance report found.')

### main begins here
myCar = []
car1 = Car('AA1234', 'Honda', 'White')
car2 = Car('NN5678', 'Nissan', 'Blue Navi')
car3 = Car('BB9999', 'Lambogini', 'Yellow')
myCar.append(car1)
myCar.append(car2)
myCar.append(car3)
for c in myCar:
  print(c)
print()
for c in sorted(myCar, reverse=True):
  print(c)
print()
car2.add_report(('25 May 2017', 'change tires', 1500))
car2.add_report(('2 June 2017', 'change lamp head', 1000))
car2.print_report()
print()
car2.add_report(('20 July 2017', 'change dish brake', 1500))
car2.max_payment()
print()
car1.max_payment()
