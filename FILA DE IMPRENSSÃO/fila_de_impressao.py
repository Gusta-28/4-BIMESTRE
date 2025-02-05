#VAMOS SIMULAR COMO FUNCIONA O ALGORITMO DE UMA IMPRESSORAQUE PODE RECEBER IMPRESSAO DE DIVERSOS COMPUTADORES, VAMOS PENSAR EM UMA FILA

#FUNÇÕES DE INTERAÇÕES COM O USUARIO
def menu():
    fila_imprenssao = FilaDeImpressao()
    #criando uma intancia para a classe
    fila_imprenssao.configurar_inicial()
    #configurar os atributos de entrada/inicial
    while True:
        #opções para o nosso usuario
        print("Opções:")
        print("1. Adicionar um trabalho na fila de imprenssão")
        print("2. imprimir o proximo trabalho da fila")
        print("3. Mostar a fila de imprenssão")
        print("4. Sair")
        escolha = imput("Escolha uma opção de 1 à 4: ")
    #aqui vai ser lido a escolha do usuario

    if escolha == "1":
        trabalho = input("Digite o nome do trabalho a ser impresso")
        #maquina da pessoa que está imprimindo
        fila_imprenssao.adicionar_trabalho(trabalho)
    elif escolha == "2":
        fila_imprenssao.processar_trabalho()
    elif escolha == "3":
        fila_imprenssao.mostrar_fila()
    elif escolha == "4":
        print("Estou me retirando deste local imundo criado por você criatura de intelecto inferior")
        break
    else:
        print("Opção inválida. escolha APENAS AS OPÇÕES DE 1 À 4.")