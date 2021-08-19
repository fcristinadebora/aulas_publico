from .departamento import Departamento #Importamos as classes que iremos utilizas

class Escola:
    def __init__(self, departamentos, estudantes = None): #O parametro estudantes é opcional, então definimos um valor padrão para quando ele não for passado
        self.__departamentos = [];
        self.__escola = [];

        if (isinstance(departamentos, list)):
            self.__departamentos = departamentos

        if (isinstance(departamentos, Departamento)):
            self.__departamentos = [departamentos]

        if (len(self.__departamentos) == 0):  # se não tiver nenhum departamento informado
            raise Exception("Falha ao instanciar Escola, obrigatório ao menos um departamento") #retorna uma exception, pois a relação entre escola de departamento é de 1:1..*, ou seja, não pode existir escola sem departamento

        self.__estudantes = []  # uma boa prática é definir os valores padrão antes, e nas condições alterá-los se necessário
        if (isinstance(estudantes, list)):
            self.__estudantes = estudantes

    def set_departamentos(self, departamentos):
        if (not isinstance(departamentos, list)):
            return

        self.__departamentos = departamentos

    def get_departamentos(self):
        return self.__departamentos

    def set_estudantes(self, estudantes):
        if (not isinstance(estudantes, list)):
            return

        self.__estudantes = estudantes

    def get_estudantes(self):
        return self.__estudantes

    estudantes = property(fget=get_estudantes, fset=get_estudantes)
    departamentos = property(fget=get_departamentos, fset=set_departamentos)

    # Método para adicionar mais 1 item à lista de estudantes
    def add_estudante(self, estudante):
        return self.__estudantes.push(estudante)

    # Método para adicionar mais 1 item à lista de departamentos
    def add_departamento(self, departamento):
        return self.__departamentos.append(departamento)