# จากไฟล์ Cities.csv และ Countries.csv ให้นิสิตเติมโปรแกรมภาษาไพท่อนดังต่อไปนี้ให้สมบูรณ์ (ส่วนที่เป็น ...) 
# โดยนิสิตสามารถเขียนคลาส ฟังชัน (ก่อน main) และหรือโค๊ด (ในส่วนของ main) เพิ่มเติมเอาได้ 
# แต่ไม่อนุญาติให้ลบส่วนของโค๊ดที่กำหนดมาให้ (ต้องปรับแก้ ...)
# หมายเหตุ ถ้าพบการใช้คำสั่ง import ใดๆ จะคิดค่าตรวจ -50% ของคะแนนที่ได้

class City:
  nbCity = 0
  def __init__(s,city,country,lat,long,temp):
    s.city = city; s.country = country; s.lat = lat
    s.long = long; s.temp = temp; City.nbCity += 1

class Country:
  nbCountry = 0
  def __init__(s,country,pop,eu,coastline):
    s.country = country; s.pop = pop; s.eu = eu
    s.coastline = coastline; Country.nbCountry += 1

def readCity():
  myCity = []
  with open('Cities.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity

def test_readCity(myCity):
  for c in myCity:
    print(c.city,c.country,c.lat,c.long,c.temp)

def readCountry():
  myCountry = []
  with open('Countries.csv') as fp:
    c = fp.readline()
    for c in fp:
      co = c.strip().split(',')
      country,pop,eu,coastline = co[0],float(co[1]),co[2],co[3]
      myCountry.append(Country(country,pop,eu,coastline))
  return myCountry

def test_readCountry(myCountry):
  for co in myCountry:
    print(co.country,co.pop,co.eu,co.coastline)

def q01(myCity, myCountry):
  for co in myCountry:
    if co.eu == 'yes' and co.coastline == 'no':
      #print(f'{co.country}: ', end='')
      coyes, sumTemp, nbCity = co.country, 0, 0
      for ci in myCity:
        if ci.country == coyes:
          sumTemp += ci.temp
          nbCity += 1
      if nbCity > 0:
        averTemp = sumTemp / nbCity
        print(f'{coyes}: {averTemp:.2f}')

def q02(myCity, myCountry):
  mydic,myMax, myMin = {}, -9999, 9999
  for co in myCountry:
    if co.eu == 'no':
      coName, sumTemp, nbCity = co.country, 0, 0
      for ci in myCity:
        if ci.country == coName:
          sumTemp += ci.temp
          nbCity += 1
      if nbCity > 0:
        averTemp = sumTemp / nbCity
        mydic[coName] = averTemp
        if averTemp > myMax:
          myMax = averTemp
        if averTemp < myMin:
          myMin = averTemp
  for co,temp in mydic.items():
    if temp == myMin:
      print(f'The lowest average city temperature: {co} ({myMin:.2f})')
    if temp == myMax:
      print(f'The highest average city temperature: {co} ({myMax:.2f})')  

### main begins here
myCity = readCity()
myCountry = readCountry()
#test_readCity(myCity)
#test_readCountry(myCountry)

"""
1. From Cities.csv and Countries.csv, show the average tempeture of 
   all countries in EU but no coastline.
>>> q01(myCity, myCountry)
Output should be:
Austria: 6.14
Czech Republic: 7.86
Hungary: 9.60
Slovakia: 8.48
2. From Cities.csv and Countries.csv, out of EU, which country has the
   lowest average city temperature and which country has the highest
   average city temperature.
>>> q02(myCity, myCountry) 
The highest average city temperature: Albania (15.18)
The lowest average city temperature: Norway (3.73)
"""
