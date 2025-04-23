# U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨

# First, ask the user to enter their grade as an integer.

# Create a four-year high school grade system using an if/elif/else statement:

#     grade is 9, print 'Freshman'
#     grade is 10, print 'Sophomore'
#     grade is 11, print 'Junior'
#     grade is 12, print 'Senior'
#     Everything else is 'TBD'

nota = int(input('Informe sua nota: '))

if nota == 9:
    print('Freshman')
elif nota == 10:
    print('Sophomore')
elif nota == 11:
    print('Junior')
elif nota == 12:
    print('Senior')
else:
    print('TBD')