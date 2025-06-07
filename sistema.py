# PROJETO PRÁTICO - DISCIPLINA [NOME DA DISCIPLINA]
# DUPLA: [NOME1], [RGM1] | [NOME2], [RGM2]
# ENTREGA: 12/06/2025 (23:59)
# PARADIGMA: PROGRAMÇÃO PROCEDURAL (SEM POO OU FRAMEWORKS)

import json
import os

# Arquivo para armazenar as tarefas
ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON ou retorna lista vazia se não existir."""
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    titulo = input("Digite o título da tarefa: ").strip()
    if not titulo:
        print("Título não pode ser vazio!")
        return
    
    tarefas = carregar_tarefas()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas cadastradas."""
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\nLista de Tarefas:")
    for tarefa in tarefas:
        status = "✓" if tarefa["concluida"] else "✗"
        print(f"{tarefa['id']}. [{status}] {tarefa['titulo']}")

def marcar_concluida():
    """Marca uma tarefa como concluída."""
    listar_tarefas()
    tarefas = carregar_tarefas()
    if not tarefas:
        return
    
    try:
        id_tarefa = int(input("Digite o ID da tarefa concluída: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                salvar_tarefas(tarefas)
                print(f"Tarefa '{tarefa['titulo']}' marcada como concluída!")
                return
        print("ID não encontrado.")
    except ValueError:
        print("ID inválido. Digite um número.")

def menu():
    """Exibe o menu principal."""
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
