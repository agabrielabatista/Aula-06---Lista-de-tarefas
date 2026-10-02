tarefas = [
    {"titulo": "estudar", "concluida": "sim", "prioridade": "alta"},
    {"titulo": "arrumar o quarto", "concluida": "nao", "prioridade": "baixa"},
    {"titulo": "lavar roupa", "concluida": "nao", "prioridade": "baixa"},
    {"titulo": "cozinhar", "concluida": "sim", "prioridade": "alta"}
]

def mostrar():
    for tarefa in tarefas:
        nome = tarefa["titulo"]
        status = tarefa["concluida"]
        prioridade = tarefa["prioridade"]
        
        if status == "sim":
            caixinha = "[x]"
        else:
            caixinha = "[ ]"
            
        print(nome, caixinha, prioridade)

def concluidas():
    for tarefa in tarefas:
        nome = tarefa["titulo"]
        status = tarefa["concluida"]
        prioridade = tarefa["prioridade"]
        
        if status == "sim":
            print(nome, "[x]", "concluida: sim", prioridade)

def pendentes():
    for tarefa in tarefas:
        nome = tarefa["titulo"]
        status = tarefa["concluida"]
        prioridade = tarefa["prioridade"]
        
        if status == "nao":
            print(nome, "[ ]", prioridade)

def prioridades():
    prioridade_buscada = input("qual prioridade você quer ver? (alta/baixa): ")
    for tarefa in tarefas:
        nome = tarefa["titulo"]
        status = tarefa["concluida"]
        prioridade = tarefa["prioridade"]
        
        if prioridade == prioridade_buscada:
            if status == "sim":
                caixinha = "[x]"
            else:
                caixinha = "[ ]"
            print(nome, caixinha, prioridade)

def cadastrar():
    titulo = input("nome da nova tarefa: ")
    prioridade = input("prioridade da tarefa (alta/baixa): ")
    
    nova_tarefa = {
        "titulo": titulo, 
        "concluida": "nao", 
        "prioridade": prioridade
    }
    
    tarefas.append(nova_tarefa)
    print("tarefa cadastrada com sucesso!")

def finalizar():
    nome_da_tarefa = input("nome da tarefa para concluir: ")
    for tarefa in tarefas:
        if tarefa["titulo"] == nome_da_tarefa:
            tarefa["concluida"] = "sim"
            print("tarefa concluída!")

def remover():
    nome_da_tarefa = input("nome da tarefa para remover: ")
    for tarefa in tarefas:
        if tarefa["titulo"] == nome_da_tarefa:
            tarefas.remove(tarefa)
            print("tarefa removida")
            break

while True:
    print("1 - mostrar todas as tarefas")
    print("2 - mostrar tarefas concluidas")
    print("3 - mostrar tarefas pendentes")
    print("4 - mostrar tarefas por prioridades")
    print("5 - cadastrar tarefa nova")
    print("6 - finalizar tarefa")
    print("7 - remover tarefa")
    print("0 - sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        mostrar()
    elif opcao == "2":
        concluidas()
    elif opcao == "3":
        pendentes()
    elif opcao == "4":
        prioridades()
    elif opcao == "5":
        cadastrar()
    elif opcao == "6":
        finalizar()
    elif opcao == "7":
        remover()
    elif opcao == "0":
        print("saindo do programa...")
        break
    else:
        print("opção inválida, tente novamente")
