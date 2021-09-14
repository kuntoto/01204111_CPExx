class Station:
  def __init__(self, id, name):
    self.sid = int(id)
    self.name = name
  def get_price(self, other):
    return abs(self.sid - other.sid)*5
  def __str__(self):
    return f'{self.sid}: {self.name}'
class BTScard:
  def __init__(self, id, value):
    self.cid = id
    self.value = value
    self.station = ''
  def __str__(self):
    return '('+str(self.cid)+','+str(self.value)+')'
  def add_value(self, x):
    self.value += x
  def enter(self, station):
    if self.station == '':
      self.station = station
      return True
    return False
  def leave(self, station):
    if self.station == '':
      return self.value,-2
    else:
      if self.value >= self.station.get_price(station):
        self.value -= self.station.get_price(station)
        self.station = ''
        return self.value,0
      else:
        return self.value,-1
  def __lt__(self, rhs):
    return self.value < rhs.value

#---------------------------------------
### main
s1 = Station(1,'Siam'); s2 = Station(3,'Mo Chit'); s3 = Station(5,'Asok')
c1 = BTScard(123, 5); c2 = BTScard(999, 10)
#---------------------------------------
print(s1,s2,s3)
print(c1,c2)
#---------------------------------------
c1.add_value(100) # c1 มีเงินในบัตร 105 บาท
print(c1)
p = c1.enter(s1) # p = True
print(c1,p)
p = c1.enter(s3) # p = False (แตะเข้าสถานีหลังจากแตะเข้าไปแล้ว)
print(c1,p)
p = c1.leave(s2) # c1 เหลือเงินในบัตร 95 บาท โดย p = (95, 0)
print(c1,p)
p = c2.enter(s3) # p = True
print(c2,p)
p = c2.leave(s1) # c2 มีเงินในบัตร 10 บาทไม่พอจ่ายค่าโดยสาร โดย p = (10, -1)
print(c2,p)
c2.add_value(50) # c2 มีเงินในบัตร 60 บาท
print(c2)
p = c2.leave(s1) # c2 เหลือเงินในบัตร 40 บาท โดย p = (40, 0)
print(c2,p)
p = c2.leave(s2) # p = (40, -2) (ยังไม่ได้แตะเข้าสถานี จึงไม่มีสถานีต้นทาง)
print(c2,p)
p = c2.enter(s2) # p = True
print(c2,p)
p = c1 < c2 # p = False
print(p)
