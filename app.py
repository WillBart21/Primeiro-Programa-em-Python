import os

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False }, 
                {"nome":"Pizza Suprema", "categoria":"Italiana", "ativo":True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
]

def exibir_nome_programa():
    """ Essa função exibe o nome estilizado do programa na tela"""

    print("""
        
        𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤

        """)


def exibir_opcoes():
    """Essa função exibe as opções disponíveis no menu principal"""

    print("1. Cadastrar Restaurante 1: ")
    print("2. Listar Restaurante 2: ")
    print("3. Alternar Estado do Restaurante 3: ")
    print("4.  Sair 4: \n")


def finalizar_app():
    """Essa função exibe a mensagem de finalização do aplicativo"""

    exibir_subtitulo("Finalizando o app")

def voltar_ao_menu_principal():
    """Essa função solicita uma tecla para retornar ao menu principal
        Outputs:
        - Retorna ao menu principal
    """

    input("\nDigite uma tecla para voltar ao menu principal!")
    main()

def opcao_invalida():
    """Essa função exibe que a opção é inválida e retorna ao menu principal
        Outputs:
        Retorna ao menu principal
    """

    os.system("cls")
    print("Opção Inválida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função exibe um subtitulo estilizado na tela
        Inputs:
        - texto: str - O texto do subtítulo
    """
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante
        
        Inputs:
        - Nome do Restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do seu restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função lista os restaurantes cadastrados na lista

        Outputs:
        - Exibe a lista de restaurantes na tela
    """
    exibir_subtitulo("Listando os restaurantes:")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}")

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "Ativado" if restaurante['ativo'] else "Desativado"
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    """Esta função alterna o estado de ativado/desativado de um restaurante já cadastrado na lista
        Outputs:
        - Exibe mensagem indicando o sucesso da operação
    """
    exibir_subtitulo("Alternando estado do restaurante")

    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem =  f"O restaurante {nome_restaurante} foi ativado com sucesso " if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
        
    voltar_ao_menu_principal()

def escolher_opcao():
    """Esta função é responsável pela escolha das opções
        Outputs:
        - Executa a opção escolhida pelo usuário
    """
    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante() 

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """ Função principal que inicia o programa """
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
