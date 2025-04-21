# The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

# It's an oversized 8 ball with some of the following answers:

#     Yes - definitely.
#     It is decidedly so.
#     Without a doubt.
#     Reply hazy, try again.
#     Ask again later.
#     Better not tell you now.
#     My sources say no.
#     Outlook not so good.
#     Very doubtful.

# Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

# The output should have the following format:

# Question:      [Question]
# Magic 8 Ball:  [Answer]

import random

pergunta = input('Pergunte algo à bola 8: ')

num = random.randint(1, 9)

print('Pergunta: ' + pergunta)

if num == 1:
  print('Bola 8 mágica: Sim - Com certeza.')
elif num == 2:
  print('Bola 8 mágica: Foi decidido assim.')
elif num == 3:
  print('Bola 8 mágica: Sem dúvida.')
elif num == 4:
  print('Bola 8 mágica: Resposta incerta, tente de novo.')
elif num == 5:
  print('Bola 8 mágica: Pergunte de novo mais tarde.')
elif num == 6:
  print('Bola 8 mágica: Melhor eu não te contar agora.')
elif num == 7:
  print('Bola 8 mágica: Minhas fontes dizem que não.')
elif num == 8:
  print('Bola 8 mágica: Perspectivas não muito boas.')
else:
  print('Bola 8 mágica: Duvidoso.')