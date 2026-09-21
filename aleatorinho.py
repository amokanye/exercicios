import random

print('Acerte o número aleatório de 1 a 100!!!' 
      "")
numeroaleatorio = random.randint(0,101)

while True:
 palpite = int(input('Qual o seu palpite? '))
 if palpite < numeroaleatorio:
  print('Palpite muito baixo! Tente um número maior. ')
 elif palpite > numeroaleatorio:
  print('Palpite muito alto! Tente um número mais baixo. ')
 elif palpite == numeroaleatorio:
  break
 
print('Parabéns! Você acertou o número aleátório. ')