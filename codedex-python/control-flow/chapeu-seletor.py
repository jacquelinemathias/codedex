# Write a program that asks the user some questions with the int() and input() functions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

#     If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
#     Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
#     Else, output the message "Wrong input."

# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

#     If the answer is 1, Hufflepuff +2.
#     Else if answer is 2, Slytherin +2.
#     Else if answer is 3, Ravenclaw +2.
#     Else if answer is 4, Gryffindor +2.
#     Else, output the message "Wrong input."

# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

#     If the answer is 1, Slytherin +4.
#     Else if the answer is 2, Hufflepuff +4.
#     Else if the answer is 3, Ravenclaw +4.
#     Else if the answer is 4, Gryffindor +4.
#     Else, output "Wrong input."

# Lastly, print out the score for each house.

# Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!

print('Você prefere o nascer (1) ou o pôr (2) do sol?')
perg1 = int(input('Resposta: '))

print('Quando eu morrer, quero ser lembrado como: 1- O Bom; 2- O Grande; 3- O Sábio; 4- O Corajoso')
perg2 = int(input('Resposta: '))

print('De qual instrumento você mais gosta? 1- Violino; 2- Trompete; 3- Piano; 4- Tambor')
perg3 = int(input('Resposta: '))

grifinoria = 0
corvinal = 0
lufalufa = 0
sonserina = 0

if perg1 == 1:
  grifinoria = grifinoria + 1
  corvinal = corvinal + 1
elif perg1 == 2:
  lufalufa = lufalufa +1
  sonserina = sonserina +1
else:
  print('Input incorreto.')

if perg2 == 1:
  lufalufa = lufalufa + 2
elif perg2 ==2:
  sonserina = sonserina + 2
elif perg2 == 3:
  corvinal = corvinal + 2
elif perg2 == 4:
  grifinoria = grifinoria + 2
else:
  print('Input incorreto')

if perg3 == 1:
  sonserina = sonserina + 4
elif perg3 == 2:
  lufalufa = lufalufa + 4
elif perg3 == 3:
  corvinal = corvinal + 4
elif perg3 == 4:
  grifinoria = grifinoria +4
else:
  print('Input incorreto.')

print('Grifinória: ', grifinoria)
print('Lufa Lufa: ', lufalufa)
print('Corvinal: ', corvinal)
print('Sonserina: ', sonserina)

if grifinoria > sonserina and grifinoria > lufalufa and grifinoria > corvinal:
    print('A casa vencedora é Grifinória com', grifinoria, 'pontos!')
elif lufalufa > sonserina and lufalufa > grifinoria and lufalufa > corvinal:
    print('A casa vencedora é Lufa Lufa com', lufalufa, 'pontos!')
elif corvinal > sonserina and corvinal > grifinoria and corvinal > lufalufa:
    print('A casa vencedora é Corvinal com', corvinal, 'pontos!')
elif sonserina > grifinoria and sonserina > lufalufa and sonserina > corvinal:
    print('A casa vencedora é Sonserina com', sonserina, 'pontos!')
else:
    print('Empate! Faça o teste novamente.')