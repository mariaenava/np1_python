lista_cursos = [
    {
        "id": "1", 
        "item": "Lógica de programação", 
        "descricao": "Curso básico para iniciantes, que ensina os fundamentos da lógica de programação. O foco é em como pensar e resolver problemas utilizando conceitos essenciais, como variáveis, operadores, estruturas de controle e algoritmos."
        },
    {
        "id": "2", 
        "item": "Desenvolvimento Web", 
        "descricao": "Curso focado no aprendizado de tecnologias para criar websites e aplicações web. Inclui conceitos de HTML, CSS, JavaScript, frameworks modernos como React, e práticas de desenvolvimento front-end e back-end para construir projetos completos."},
    {
        "id": "3", 
        "item": "Desenvolvimento Mobile", 
        "descricao": "Este curso ensina como desenvolver aplicativos para dispositivos móveis utilizando frameworks populares, como Flutter e React Native, além de capacitar para o desenvolvimento nativo em Android (Kotlin) e iOS (Swift), abrangendo desde a criação até a publicação nas lojas de aplicativos."
        },
    {
        "id": "4", 
        "item": "Análise e Ciência de Dados", 
        "descricao": "Curso direcionado ao processamento e análise de dados. Abrange técnicas de coleta, limpeza, visualização e análise estatística, além do uso de ferramentas como Python, Matplotlib, Seaborn e bibliotecas de análise de dados para extrair informações úteis e tomar decisões baseadas em dados."
        },
    {
        "id": "5", 
        "item": "Inteligência Artificial", 
        "descricao": "Curso introdutório à Inteligência Artificial, abordando os principais conceitos, como aprendizado supervisionado, não supervisionado e redes neurais. O curso também inclui a implementação de IA em projetos práticos utilizando algoritmos de aprendizado de máquina."
        },
    {
        "id": "6", 
        "item": "Cybersegurança", 
        "descricao": "Curso voltado para a segurança digital, abordando temas como proteção de dados, criptografia, testes de penetração (pentesting), análise de vulnerabilidades e defesa contra ataques cibernéticos. O objetivo é preparar profissionais para proteger sistemas e redes contra ameaças digitais."
        },
    {
        "id": "7", 
        "item": "Voltar ao menu inicial", 
        "descricao": None
        }
]


lista_modulos = [
    {"id":"1", "id_curso": "1", "id_modulo": "1", "item":"Fundamentos de Lógica de Programação"},
    {"id":"2", "id_curso": "1", "id_modulo": "2", "item":"Operadores e Controle de Fluxo"},
    {"id":"3", "id_curso": "1", "id_modulo": "3", "item":"Estruturas de Dados Simples"},
    {"id":"4", "id_curso": "1", "id_modulo": "4", "item":"Algoritmos de Ordenação e Busca"},
    {"id":"5", "id_curso": "1", "id_modulo": "5", "item":"Desenvolvimento de Projetos Práticos"},

    {"id":"6", "id_curso": "2", "id_modulo": "1", "item":"Fundamentos de HTML e CSS"},
    {"id":"7", "id_curso": "2", "id_modulo": "2", "item":"Introdução ao JavaScript"},
    {"id":"8", "id_curso": "2", "id_modulo": "3", "item":"Desenvolvimento de Aplicações com React.js"},
    {"id":"9", "id_curso": "2", "id_modulo": "4", "item":"Desenvolvimento de Back-End com Node.js"},
    {"id":"10", "id_curso": "2", "id_modulo": "5", "item":"Deploy de Aplicações Web"},

    {"id":"11", "id_curso": "3", "id_modulo": "1", "item":"Introdução ao Desenvolvimento Mobile com Flutter"},
    {"id":"12", "id_curso": "3", "id_modulo": "2", "item":"Fundamentos do React Native"},
    {"id":"13", "id_curso": "3", "id_modulo": "3", "item":"Desenvolvimento Android Nativo com Kotlin"},
    {"id":"14", "id_curso": "3", "id_modulo": "4", "item":"Desenvolvimento iOS com Swift"},
    {"id":"15", "id_curso": "3", "id_modulo": "5", "item":"Publicação de Aplicativos nas Stores"},

    {"id":"16", "id_curso": "4", "id_modulo": "1", "item":"Introdução à Análise de Dados com Python"},
    {"id":"17", "id_curso": "4", "id_modulo": "2", "item":"Visualização de Dados com Matplotlib e Seaborn"},
    {"id":"18", "id_curso": "4", "id_modulo": "3", "item":"Análise Estatística de Dados"},
    {"id":"19", "id_curso": "4", "id_modulo": "4", "item":"Trabalhando com Grandes Conjuntos de Dados"},
    {"id":"20", "id_curso": "4", "id_modulo": "5", "item":"Projetos de Análise de Dados"},

    {"id":"21", "id_curso": "5", "id_modulo": "1", "item":"Fundamentos de Inteligência Artificial"},
    {"id":"22", "id_curso": "5", "id_modulo": "2", "item":"Aprendizado Supervisionado"},
    {"id":"23", "id_curso": "5", "id_modulo": "3", "item":"Aprendizado Não Supervisionado"},
    {"id":"24", "id_curso": "5", "id_modulo": "4", "item":"Redes Neurais e Deep Learning"},
    {"id":"25", "id_curso": "5", "id_modulo": "5", "item":"Implementação de IA em Projetos Práticos"},

    {"id":"26", "id_curso": "6", "id_modulo": "1", "item":"Fundamentos de Segurança da Informação"},
    {"id":"27", "id_curso": "6", "id_modulo": "2", "item":"Criptografia e Segurança de Dados"},
    {"id":"28", "id_curso": "6", "id_modulo": "3", "item":"Testes de Penetração (Pentesting)"},
    {"id":"29", "id_curso": "6", "id_modulo": "4", "item":"Segurança em Aplicações Web"},
    {"id":"30", "id_curso": "6", "id_modulo": "5", "item":"Gestão de Incidentes e Resposta a Ataques Cibernéticos"}
]

def cursos():
    menu_cursos()
    navegacao_menu_cursos()

def modulos():
    menu_modulos()

def menu_cursos():
    print("\n")
    print("=" * 10, "CURSOS DISPONÍVEIS", "=" * 10, end="\n"*2)

    for linha in lista_cursos:
        print(f'{linha["id"]}. {linha["item"]}')
    print("\n")

def navegacao_menu_cursos():
    while True:
        escolha = input("---> Quer saber mais? Escolha uma das opções acima: ")
        if escolha in ["1", "2", "3", "4", "5", "6"]:
            conteudo_menu_cursos(escolha)
            input("---> Para voltar ao menu de cursos disponíveis, pressione enter no seu teclado. ")
            menu_cursos()
        elif escolha == "7":
            return
        else:
            print("\n")
            print("->->-> Opção inválida. Tente novamente e escolha uma das opções acima <-<-<-", end="\n")

def conteudo_menu_cursos(escolha):
    for linha in lista_cursos:
        if escolha == linha["id"]:
            print("\n")
            print("-" * 5, (linha["item"]).upper(), "-" * 5, end="\n"*2)
            print("Descrição:", (linha["descricao"]), end="\n"*2)
            print("Módulos do Curso:", end="\n")
    for linha in lista_modulos:
        if escolha == linha["id_curso"]:
            print(f'{linha["id_modulo"]}. {linha["item"]}')
    print("\n")

def menu_modulos():
    print("\n")
    print("=" * 10, "MÓDULOS DOS CURSOS", "=" * 10, end="\n" * 2)

    for curso in lista_cursos:
        if curso["id"] != "7":
            print("-" * 3, curso["item"], "-" * 3)
            for modulo in lista_modulos:
                if modulo["id_curso"] == curso["id"]:
                    print(f'  {modulo["id_modulo"]}. {modulo["item"]}')
            print("\n")
    input("---> Para voltar ao menu inicial, pressione enter no seu teclado. ")