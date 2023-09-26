import datetime
a = '\033[4mEvent Countdown Timer\033[0m'
print(f'\033[1;33m{a}')
print()

event = input('Enter the event: ')
print()
ask = int(input('\033[0mEnter the year: '))
ask2 = int(input('Enter the month: '))
ask3 = int(input('Enter the day: '))

b = datetime.date(ask, ask2, ask3)
c = datetime.date.today()
e = (c - b).days
f = abs(e)

print ()
if e < 0:
  print(f'{event} is {f} days from today😎😎')
elif e > 0:
  print(f'{event} took place {f} days ago 😥😥')
else:
  print(f'Hurrayyy!! 🥳 {event} is today 🤩🥳')