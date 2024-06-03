import os

lista_de_tarefas = []
status = ["pendente", "concluída"]


def clear_console():
    os.system('cls')

def adcionar_tarefa(atividade):
    tarefa = {'tarefa': f'{atividade}','status': f'{status[0]}'}
    lista_de_tarefas.append(tarefa)

def remover_tarefa(tarefa):
    for i in lista_de_tarefas:
        if i['tarefa'] == tarefa:
            lista_de_tarefas.remove(i)
            clear_console()
            return print("Tarefa removida")
    clear_console()
    return print(f"tarefa '{tarefa}' não encontrada")

def listar_tarefas():
    for i in lista_de_tarefas:
        print(f"{i['tarefa']} - {i['status']}")

def marcar_como_concluida(lista, tarefa):
    for i in lista:
        if i['tarefa'] == tarefa:
            i['status'] = status[1]
            clear_console()
            return print("Tarefa Concluída\n")
    clear_console()
    return print(f"tarefa '{tarefa}' não encontrada")

opcao = 0

while opcao != 5:

    print(
        "O que deseja fazer: \n" +
        "1 - Adicionar uma nova tarefa.\n" +
        "2 - Remover uma tarefa existente.\n" +
        "3 - Listar todas as tarefas pendentes.\n" +
        "4 - Marcar uma tarefa como concluída.\n" +
        "5 - Sair"
    )
    
    opcao = int(input())

    clear_console()

    if opcao == 1:

        tarefa = input("Diga qual tarefa vai Adcionar: ")
        adcionar_tarefa(tarefa)
        clear_console()
        print(f"a seguinte tarefa foi adcionada : {tarefa}")
        input("Aperte ENTER para continuar")

    elif opcao == 2:
        clear_console()
        listar_tarefas()
        tarefa = input("Diga qual tarefa vai Remover: ")
        remover_tarefa(tarefa)
        input("Aperte ENTER para continuar")

    elif opcao == 3:

        listar_tarefas()
        input("Aperte ENTER para continuar")

    elif opcao == 4:
        listar_tarefas()
        tarefa = input("Diga qual tarefa esta Concluída: ")
        clear_console()
        marcar_como_concluida(lista_de_tarefas , tarefa)
        input("Aperte ENTER para continuar")
    
    clear_console()
         

print("Programa finalizado!")
input()
clear_console()
