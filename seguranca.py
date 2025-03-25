lista_seguranca = [
    {
        "id": "1",
        "item": "Conceitos Essenciais de Segurança de Dados",
        "descricao": "A segurança de dados protege suas informações pessoais contra acessos indevidos e ataques cibernéticos.",
        "topicos": [
            "Dados pessoais incluem nome, e-mail e CPF, enquanto dados sensíveis englobam informações como saúde e biometria.",
            "Principais ameaças incluem phishing (golpes por e-mail), malware (vírus) e engenharia social (manipulação para obter dados).",
            "Para se proteger, nunca compartilhe senhas, desconfie de mensagens suspeitas e mantenha seus dispositivos atualizados."
        ]
        },
    {
        "id": "2",
        "item": "LGPD (Lei Geral de Proteção de Dados)",
        "descricao": "A LGPD regula a coleta, armazenamento e uso de dados pessoais, garantindo mais privacidade e transparência.",
        "topicos": [
            "Você tem o direito de saber quais dados estão sendo coletados e para qual finalidade.",
            "Pode solicitar a correção ou exclusão dos seus dados a qualquer momento.",
            "Aqui na plataforma, seguimos as diretrizes da LGPD para garantir sua segurança e privacidade."
        ]
        },
    {
        "id": "3",
        "item": "Boas Práticas para Navegação Segura",
        "descricao": "Adotar hábitos seguros ao navegar na internet ajuda a evitar ataques e proteger suas informações.",
        "topicos": [
            "Use senhas longas e seguras, misturando letras, números e símbolos. Evite combinações óbvias.",
            "Ative a autenticação em dois fatores (2FA) para aumentar a segurança das suas contas.",
            "Desconfie de links e anexos desconhecidos em e-mails e mensagens.",
            "Evite reutilizar senhas em diferentes sites para minimizar riscos caso uma delas seja vazada."
        ]
        },
    {
        "id": "4",
        "item": "Segurança em Plataformas Educacionais",
        "descricao": "Ao usar plataformas de ensino online, mantenha suas credenciais seguras e evite compartilhar informações sensíveis.",
        "topicos": [
            "Nunca compartilhe sua senha com terceiros, mesmo que pareçam confiáveis.",
            "Desconfie de e-mails suspeitos pedindo seus dados pessoais ou bancários.",
            "Evite divulgar informações como telefone e endereço em fóruns e chats públicos.",
            "Caso perceba atividades incomuns na sua conta, altere sua senha imediatamente."
        ]
        },
    {
        "id": "5",
        "item": "Segurança em Dispositivos e Conexões",
        "descricao": "Proteger seus dispositivos e conexões é essencial para evitar acessos indesejados aos seus dados.",
        "topicos": [
            "Evite redes Wi-Fi públicas sem proteção, pois elas podem ser monitoradas por hackers.",
            "Mantenha seu sistema operacional e aplicativos sempre atualizados para evitar vulnerabilidades.",
            "Use um bom antivírus para identificar e bloquear ameaças antes que comprometam seu dispositivo.",
            "Nunca salve senhas em computadores públicos. Prefira usar um gerenciador de senhas seguro."
            ]
        },
    {
        "id": "6",
        "item": "Voltar ao menu inicial",
        "descricao": None,
        "topicos": None
        }
]


def seguranca():
    menu_seguranca()
    navegacao_menu_seguranca()

def menu_seguranca():
    print("\n")
    print("=" * 10, "INFORMAÇÕES DE SEGURANÇA", "=" * 10, end="\n"*2)

    for linha in lista_seguranca:
        print(f'{linha["id"]}. {linha["item"]}')
    print("\n")


def navegacao_menu_seguranca():
    while True:
        escolha = input("---> Quer saber mais? Escolha uma das opções acima: ")
        if escolha in ["1", "2", "3", "4", "5"]:
            conteudo_menu_seguranca(escolha)
            input("---> Para voltar ao menu de informações de segurança, pressione enter no seu teclado. ")
            menu_seguranca()
        elif escolha == "6":
            return
        else:
            print("\n")
            print("->->-> Opção inválida. Tente novamente e escolha uma das opções acima <-<-<-", end="\n")

def conteudo_menu_seguranca(escolha):
    for linha in lista_seguranca:
        if escolha == linha["id"]:
            print("\n")
            print("-" * 5, (linha["item"]).upper(), "-" * 5, end="\n"*2)
            print((linha["descricao"]), end="\n")
            for topico in linha["topicos"]:
                print("-", topico, end="\n")
            print("\n")