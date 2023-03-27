#Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
#programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.

#Integrantes: Victor Gabriel Guimarães, Lucas Rullo Takimoto e Mateus José Felix Silverio.

t1 = 0
t2 = 1
cont = 0

nextT = t1 + t2


n = int(input("Digite o N: "))
Prim = int(input("Digite o Prim: "))

           
while (cont < n):
    if (nextT > Prim):
        print("{}".format(nextT))
    t1 = t2
    t2 = nextT
    nextT = t1 + t2
    cont+= 1

print("\n\nFim do Programa")
