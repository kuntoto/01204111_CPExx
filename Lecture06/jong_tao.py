def printMenu():
  s = '''Select menu :
1. add flight data
2. flight data by code
3. show all flight data
4. flight booking
5. show people flight data
6. exit'''
  print(s)
  
def addFlightData():
  r = {}
  data = input('Add data : ').split()
  r['flightNb'] = data[0]
  r['source'] = data[1]
  r['dest'] = data[3]
  r['booked'] = int(data[4])
  r['seats'] = int(data[6])
  return r

def searchFlight(flight):
  flightNb = input('Enter code : ')
  for f in flight:
    if f['flightNb']==flightNb:
      print(f"{flightNb} is from {f['source']} to {f['dest']}, number of people booking is {f['booked']}/{f['seats']}")
      break

def printAllFlights(flight):
  print('All flight data')
  for f in flight:
    print(f"{f['flightNb']} is from {f['source']} to {f['dest']}, number of people booking is {f['booked']}/{f['seats']}")

def flightBooking(flight):
  book = {}
  name = input('Enter your name : ')
  code = input('Enter flight code : ')
  for f in flight:
    if f['flightNb']==code:
      #print(f"-> available seats {f['booked']}/{f['seats']}")
      if f['booked'] < f['seats']:
        f['booked'] += 1
        book[name] = code
        print('Success')
      else:
        print(f"The flight is full, Sorry")
        return book
  return book
  
def printBooking(booking):
  myBook = {}
  for i in booking:
    try:
      k, v = list(i.items())[0][0], list(i.items())[0][1]
    except:
      continue
    #print(k, v, myBook)
    if k in myBook.keys():
      myBook[k].append(v)
    else:
      myBook[k] = []
      myBook[k].append(v)
  name = input('Enter your name : ')
  print(f"{name} is booking flight code = ", end='') 
  for i in myBook[name]:
    print(f"{i}", end=' ')
  print() 
      
def myMain():
  flight, booking = [], []
  printMenu()
  while True:
    m = int(input('menu : '))
    if m==6:
      print('EXIT!!!!!!!!!!!!!!!')
      break
    elif m==1:
      r = addFlightData()
      flight.append(r)
    elif m==2:
      searchFlight(flight)
    elif m==3:
      printAllFlights(flight)
    elif m==4:
      #printAllFlights(flight)
      booking.append(flightBooking(flight))
    elif m==5:
      printBooking(booking)

##--------------------------------------------------------
# A proposed solution to 04 L06 Jong Tao
# https://elab.cpe.ku.ac.th/elab/lab/1023/11703/19162/
##--------------------------------------------------------
## main begins here
myMain()   
