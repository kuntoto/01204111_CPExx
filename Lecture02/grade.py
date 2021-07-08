score = int(input('Enter your score : '))

while score < 0 or score > 100:
  score = int(input('Error score... Enter your score again : '))

grade = ''
if score >= 80:
  grade = 'A'
elif score >= 70:
  grade = 'B'
elif score >= 60:
  grade = 'C'
elif score >= 50:
  grade = 'D'
else:
  grade = 'F'

print('Grade', grade)
