import os
import time
laco = 1

print('\t bem vindo a calculadora do lucasrq')


def somar(n1, n2):
    return n2 + n1


def subtrair(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1


def dividir(n1, n2):
    return n1 / n2


def multiplicar(n1, n2):
    return n1 * n2


def limpar():
    os.system('cls')


while True:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite o segundo numero: '))
    print("\tNumero 1: ", n1)
    print("\tNumero 2: ", n2)
    limpar()
    print("digite 1 para somar: ", somar(n1, n2))
    print("digite 2 para subtrair: ", subtrair(n1, n2))
    print("digite 4 para multiplicar: ", dividir(n1, n2))
    print("digite 3 para dividir: ", multiplicar(n1, n2))
    for c in range(10):
        print(c)
        time.sleep(0.5)
    limpar()
