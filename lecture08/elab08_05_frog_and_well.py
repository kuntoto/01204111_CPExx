def frog(deep, up, down):
  if up-down <= 0 and up != deep:
    print('The frog will never escape from the well.')
  else:
    day = 0
    while deep > 0:
      day = day + 1
      if up <= deep:
        deep = deep - up
        if deep != 0:
          print(f'On day {day} the frog leaps to the depth of {deep} meters.')
        if deep == 0:
          print(f'The frog is free on day {day}.')
      else:
        print(f'The frog is free on day {day}.')
        deep = 0
      if deep > 0:
        deep = deep + down
        print(f'At night he slips down to the depth of {deep} meters.')

deep = int(input('How deep is the well? '))
up = int(input('How high the frog can jump up? '))
down = int(input('How far the frog slips down? '))
frog(deep,up,down)