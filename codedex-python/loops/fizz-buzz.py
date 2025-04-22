# Create a fizz_buzz.py program that outputs numbers from 1 to 100.

# Here's the catch:

#     For multiples of 3, print "Fizz" instead of the number.
#     For multiples of 5, print "Buzz" instead of the number.
#     Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

for numero in range (100):
  if numero % 3 == 0 and numero % 5 == 0:
    print('FizzBuzz')
  elif numero % 3 == 0:
    print('Fizz')
  elif numero % 5 == 0:
    print('Buzz')
  else:
    print(numero)