# app.py

tarefas = []
contador_id = 1  # usado pra gerar IDs únicos

def adicionar_tarefa():
    global contador_id
    print("\n--- Nova Tarefa ---")
    titulo = input("Título: ")
    descricao = input("Descrição: ")

    nova_tarefa = {
        "id": contador_id,
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }

    tarefas.append(nova_tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!\n")
    contador_id += 1

def mostrar_tarefas():
    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada ainda.\n")
        return

    for t in tarefas:
        print(f"[{t['id']}] {t['titulo']}")
        print(f"    Descrição: {t['descricao']}")
        print(f"    Status: {t['status']}")
        print("-" * 40)
    print()

def concluir_tarefa():
    try:
        id_alvo = int(input("ID da tarefa que foi concluída: "))
        for t in tarefas:
            if t["id"] == id_alvo:
                if t["status"] == "Concluída":
                    print("Essa já tá concluída, jovem!\n")
                else:
                    t["status"] = "Concluída"
                    print("Boa! Tarefa marcada como concluída.\n")
                return
        print("Não encontrei nenhuma tarefa com esse ID.\n")
    except ValueError:
        print("ID inválido.\n")

def remover_tarefa():
    try:
        id_alvo = int(input("ID da tarefa que quer remover: "))
        for t in tarefas:
            if t["id"] == id_alvo:
                tarefas.remove(t)
                print("Tarefa removida com sucesso!\n")
                return
        print("ID não encontrado.\n")
    except ValueError:
        print("ID inválido.\n")

def menu():
    while True:
        print("========== MENU ==========")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Marcar como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            mostrar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Fechando o programa... até mais!")
            break
        else:
            print("Opção inválida. Tenta de novo.\n")

# Roda o menu principal
if __name__ == "__main__":
    menu()