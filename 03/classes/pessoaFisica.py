from .pessoa import Pessoa  # primeiro importamos a classe Mãe

class PessoaFisica(Pessoa):  # Para indicar que uma classe extende a outra, passamos ela como "Parâmetro" na definição da class
    def __init__(self, nome, endereco, cpf, nascimento):
        super().__init__(nome, endereco)  # a instrução super() chama em uma classe filha, um método da classe pai. Nesse caso, está chamando o método construtor
        self.__cpf = cpf
        self.__nascimento = nascimento

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento

    def get_nascimento(self):
        return self.__nascimento

    cpf = property(get_cpf, set_cpf)
    nascimento = property(get_nascimento, set_nascimento)

    def imprimir_detalhes(self):
        print('Chamando na classe pessoaFisica')
        super().imprimir_detalhes()
        print('CPF ' + self.cpf)
        print('Nascimento ' + self.nascimento)

    def comprar(self, produto, quantidade):
        super().comprar(produto)
        print(' em ' + str(quantidade) + ' unidades')