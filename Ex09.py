#Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
#termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
#ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
#0 e 1.

#Integrantes: Victor Gabriel Guimarães, Lucas Rullo Takimoto e Mateus José Felix Silverio.

t1 = 0
t2 = 1
cont = 2

nextT = t1 + t2



n = int(input("Digite o N: "))

print("Sequencia de fibonacci \n{} \n{}".format(t1, t2))
           
while (cont < n):
    print("{}".format(nextT))
    t1 = t2
    t2 = nextT
    nextT = t1 + t2
    cont+= 1

print("\n\nFim do Programa")





