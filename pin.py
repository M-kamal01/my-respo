pin = '2332'
F = False
pin_attempts = 4
inp = input('Enter your pin : ') 
attempts = 0
while F == False and pin!=inp:
      print('Wrong pin, try again')
      inp= input('Enter your pin : ')
      if attempts == 2:
           F == True
      else:
          attempts += 1
if F == True and pin>= pin_attempts:
              print('access denied')
else: 
       print('Success');
      