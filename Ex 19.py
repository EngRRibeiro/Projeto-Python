#Sorteando um item na lista
import random  #from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quaro aluno: '))
lista = [n1,n2,n3,n4]

x = random.choice(lista) # x = choice(lista)
print ('O aluno escolhido foi {}'.format(x))