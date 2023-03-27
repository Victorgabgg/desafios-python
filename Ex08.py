# Desenvolva  um  programa  que  leia  do  teclado  um  número  inteiro  e  mostre  na  tela  se  esse  número  é primo ou não.
#Lembrando: um número primo é divisível somente por 1 e por ele mesmo.

#Integrantes: Victor Gabriel Guimarães, Lucas Rullo Takimoto e Mateus José Felix Silverio.

num = int(input("Digite um numero para checar se é primo: "))
n = 1
cont = 0

while n <= num:
   #print("Calculando...")
   if (num % n == 0):
      cont+= 1
   n+= 1
      
if (cont == 2):
    print("O numero {} é primo.".format(num))
else:
    print("O numero {} não é primo.".format(num))

print("\n\nFim do Programa")

