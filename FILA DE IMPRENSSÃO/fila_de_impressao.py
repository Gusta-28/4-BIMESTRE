#VAMOS SIMULAR COMO FUNCIONA O ALGORITMO DE UMA IMPRESSORAQUE PODE RECEBER IMPRESSAO DE DIVERSOS COMPUTADORES, VAMOS PENSAR EM UMA FILA
class FilaDeImpressao:

    def configurar_inicial(self):
        self.fila= []
#isso vai aguardar a fila de impressao no vetor fila

    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)
        print(f"Trabalho '{trabalho}' adicionado na fila de impressão.")

#remover o trabalho da lista
    def processar_trabalho(self):
        if not self.fila_vazia(): #verificar se a lista nao esta vazia
            trabalho = self.fila.pop(0) #remover o trabalho da lista
            print(f" o trabalho '{trabalho}' está sendo processado...")
        else:
            print("a fila está fazia, igual o seu coração QUE NÃO RECEBE AMOR RECIPROCO A MUITO TEMPO.")


    def mostrar_fila(self):
        if self.fila_vazia():
            print("A fila está vazia igual o amor dela por você INUTIL.")
        else:
            print("fila atual de impressão:")
            for trabalho in self.fila:
                print(f"-{trabalho}") #imprimir cada trabalho da lista

    def esta_vazia(self):
        return len(self.fila) == 0
#len verifica se o tamannho do vetor fila esta zerado

#FUNÇÕES DE INTERAÇÕES COM O USUARIO
def menu():
    fila_imprenssao= FilaDeImpressao()
    #criando uma intancia para a classe
    fila_imprenssao.configurar_inicial()
    #configurar os atributos de entrada/inicial
    while True:
        #opções para o nosso usuario
        print("\nOpções:")
        print("1. Adicionar um trabalho na fila de imprenssão")
        print("2. imprimir o proximo trabalho da fila")
        print("3. Mostar a fila de imprenssão")
        print("4. Sair")
        escolha = input("Escolha uma opção de 1 à 4 SEU MERO HUMANO: ")
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
            print("Opção inválida. escolha APENAS AS OPÇÕES DO 1 AO 4 SEU ANIMAL IMUNDO.")

menu()