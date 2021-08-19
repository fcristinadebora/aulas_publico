class Pessoa:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco

    endereco = property(get_endereco, set_endereco)
    nome = property(get_nome, set_nome)

    def imprimir_detalhes(self):
        print('Método na classe pai')
        print('Nome: ' + self.nome)
        print('Endereco ' + self.endereco)

    def comprar(self, produto):
        print("Eu " + self.__nome + " vou comprar um(a) " + produto)