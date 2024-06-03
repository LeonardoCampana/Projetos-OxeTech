import os
import math

def clear_console():
    os.system('cls')

def calcular_media(array):
    a = 0
    for i in array:
        a += int(i)

    return a / len(array)

def calcular_mediana(array):
    tamanho_array = len(array)
    if tamanho_array % 2 == 0:
        tamanho_array //= 2
        mediana = (int(array[tamanho_array]) + int(array[tamanho_array - 1])) / 2
        return print(f"Mediana : {mediana}")
    else:
        tamanho_array //= 2
        mediana = int(array[tamanho_array])
        return print(f"Mediana : {mediana}")

def calcular_moda(array):
    modas = []
    freq = 1
    max_freq = 1
    number = array[0]

    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            freq += 1
        else:
            freq = 1
        
        if freq > max_freq:
            max_freq = freq
            modas = [array[i]]
        elif freq == max_freq:
            modas.append(array[i])

    return print(f"Modas: {modas}")

def calcular_desvio_padrao(array):
    media = calcular_media(array)
    array_diferenca_quadrado = []
    for i in array:
        quadrado_diferenca = pow(int(i) - media, 2)
        array_diferenca_quadrado.append(quadrado_diferenca)
    
    media_final = 0

    for i in array_diferenca_quadrado:
        media_final += i

    media_final = media_final / len(array_diferenca_quadrado)
    resultado = math.sqrt(media_final)
    return print(f"Desvio Padrão: {resultado}")


numbers = input("Digite os numeros para os calculos (separe por espaço ex: 1 321 4 ...)\n\n")
array = numbers.split(' ', -1)
array.sort()

clear_console()

opcao = 0


while opcao != 6:

    print(
        "O que deseja fazer: \n" +
        "1 - Calcular a média dos números fornecidos\n" +
        "2 - Calcular a mediana dos números fornecidos.\n" +
        "3 - Calcular a moda dos números fornecidos.\n" +
        "4 - Calcular o desvio padrão dos números fornecidos.\n" +
        "5 - Digitar outros números\n" +
        "6 - Sair"
    )
    
    opcao = int(input())

    clear_console()

    if opcao == 1:
        media = calcular_media(array)
        print(f"Média: {media}")
        input("\nPrecione ENTER para continuar")
        
    elif opcao == 2:
        calcular_mediana(array)
        input("\nPrecione ENTER para continuar")

    elif opcao == 3:
        calcular_moda(array)
        input("\nPrecione ENTER para continuar")

    elif opcao == 4:
        calcular_desvio_padrao(array)
        input("\nPrecione ENTER para continuar")

    elif opcao == 5:
        numbers = input("Digite os numeros para os calculos (separe por espaço ex: 1 321 4 ...)\n\n")
        array = numbers.split(' ', -1)
        array.sort()
        print(f"Novos números: {array}")
        input("\nPrecione ENTER para continuar")
    
    clear_console()
         

print("Programa finalizado!")
input()
clear_console()