import sys
from cadastro import cadastro
from login import login
from cursos import cursos, modulos
from seguranca import seguranca
from salvarusuarios import carregar_usuarios

usuarios = carregar_usuarios()
usuario_logado = None

lista_menu = [
    {"id": "1", "item": "Cadastro"},
    {"id": "2", "item": "Login"},
    {"id": "3", "item": "Cursos Disponíveis"},
    {"id": "4", "item": "Módulos dos Cursos"},
    {"id": "5", "item": "Informações de Segurança"},
    {"id": "6", "item": "Sair"},
]


def main():
    global usuario_logado
    while True:
        menu_inicial()
        escolha = escolha_menu_inicial()
        usuario_logado = navegacao_menu_inicial(escolha)


def menu_inicial():
    print("=" * 69)
    print("=" * 15, "PLATAFORMA DE EDUCAÇÃO DIGITAL SEGURA", "=" * 15)
    print("=" * 69, end="\n" * 2)
    
    if usuario_logado:
        print(f"Bem-vindo à Plataforma, {usuario_logado}! Escolha uma das opções abaixo:", end="\n" * 2)
    else:
        print("Bem-vindo à Plataforma! Escolha uma das opções abaixo:", end="\n" * 2)
    
    for linha in lista_menu:
        print(f'{linha["id"]}. {linha["item"]}')
    print("\n")


def escolha_menu_inicial():
    while True:
        escolha = input("---> Opção escolhida: ")
        if escolha in ["1", "2", "3", "4", "5"]:
            return escolha
        elif escolha == "6":
            print("\n")
            sys.exit("Você saiu da Plataforma. Até a próxima!\n")
        else:
            print("\n")
            print("->->-> Opção inválida. Tente novamente e escolha uma das opções acima", end="\n")


def navegacao_menu_inicial(escolha):
    global usuario_logado
    if escolha == "1":
        usuario_logado = cadastro()
    elif escolha == "2":
        usuario_logado = login()
    elif escolha == "3":
        cursos()
    elif escolha == "4":
        modulos()
    elif escolha == "5":
        seguranca()
    print("\nVoltando ao menu inicial...\n")
    return usuario_logado


if __name__ == "__main__":
    main()