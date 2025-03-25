import re
from salvarusuarios import carregar_usuarios, salvar_usuarios

usuarios = carregar_usuarios()

def validar_senha(senha):
    if len(senha) < 8 or not any(char.isupper() for char in senha) or not re.search(r"[!@#$&_.,]", senha) or not any(char.isdigit() for char in senha):
        print("\n---> Tente novamente! A sua senha deve ter pelo menos:\n- 8 caracteres\n- Uma letra maiúscula\n- Um número\n- Um caracter especial (!@#$&_.,)", end="\n"*2)
        return False
    return True

def validar_usuario(usuario):
    if len(usuario) < 4:
      print("\n---> O nome de usuário deve ter pelo menos 4 caracteres.", end="\n"*2)
      return False
    return True


def cadastro():
    print("\n")
    print("=" * 10, "CADASTRO DE USUÁRIOS", "=" * 10, end="\n"*2)
    while True:
     usuario = input("Crie seu nome de usuário: ")
    
     if usuario in usuarios:
        print("\n---> Este usuário já existe. Tente novamente!", end="\n"*2)
     elif validar_usuario(usuario):
      break
    
    while True:
        senha = input("Crie sua senha: ")
        if validar_senha(senha): 
            break

    usuarios[usuario] = senha
    salvar_usuarios(usuarios)
    print(f"\n---> Cadastro realizado com sucesso! Bem-vindo à nossa Plataforma, {usuario}.", end="\n"*2)