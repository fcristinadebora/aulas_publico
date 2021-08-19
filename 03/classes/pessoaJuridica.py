from .pessoa import Pessoa  # primeiro importamos a classe Mãe

class PessoaJuridica(Pessoa):
    def __init__(self, nome, endereco, cnpj, nome_fantasia):
        super().__init__(nome, endereco)
        self.__cnpj = cnpj
        self.__nome_fantasia = nome_fantasia

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj

    def set_nome_fantasia(self, nome_fantasia):
        self.__nome_fantasia = nome_fantasia

    def get_nome_fantasia(self):
        return self.__nome_fantasia

    cnpj = property(get_cnpj, set_cnpj)
    nome_fantasia = property(get_nome_fantasia, set_nome_fantasia)

    def imprimir_detalhes(self):
        print('Chamando na classe pessoaJuridica')
        super().imprimir_detalhes()
        print('CNPJ ' + self.cnpj)
        print('Nome Fantasia ' + self.nome_fantasia)