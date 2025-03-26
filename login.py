from salvarusuarios import carregar_usuarios

usuarios = carregar_usuarios()

def login():
    print("\n")
    print("=" * 10, "FAÇA SEU LOGIN", "=" * 10, end="\n"*2)
    
    while True:
        usuario = input("Nome de usuário: ")
        
        if usuario not in usuarios:
            print("\n---> Usuário não encontrado. Tente novamente!", end="\n"*2)
        else:
            break  
    tentativas = 3  
    while tentativas > 0:
        senha = input("Senha: ")
        
        if usuarios[usuario] == senha:
            print(f"\n---> Login bem-sucedido! Bem-vindo de volta, {usuario}!", end="\n"*2)
            return True  
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"\n---> Senha incorreta. Você possui mais {tentativas} tentativas!", end="\n"*2)
    
    print("\n---> Número máximo de tentativas excedido. Tente novamente mais tarde!", end="\n"*2)
    return False 

