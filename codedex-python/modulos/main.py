# Create a new file called main.py.

# Import both the datetime module as well as bday_messages (the last file).

# import datetime, bday_messages

# Next, use the datetime module to create two date objects:

# today: Today's date, using the datetime.date.today() method.
# next_birthday: The date for your next birthday, using the year, month, and day arguments.
# A really cool thing you can do with date objects is addition and subtraction!

# time_difference = date1 - date2

# Use date subtraction to calculate how many days away today is from next_birthday. Then, assign the result to a new variable called days_away.

# Then, create a control flow statement:

# If today is equal to next_birthday, print the random_message variable (imported from bday_messages).
# Else, print 'My next birthday is {days_away} days away!'.

import datetime
import mensagem_aniversario

hoje = datetime.date.today()
prox_aniver = datetime.date(2000, 5, 15)
diferenca = prox_aniver - hoje

if hoje == prox_aniver:
    print(mensagem_aleatoria)
else:
    print(f'Meu aniversário é daqui' {diferenca} 'dias!')