from classes.departamento import Departamento
from classes.escola import Escola

# Instanciando departamentos
departamento_humanas = Departamento('Ciências humanas')
departamento_exatas = Departamento('Ciências exatas')

# escola_sem_departamento = Escola('lalalala') #deve disparar um erro
escola_com_departamento = Escola(departamento_exatas) #deve disparar um erro

departamentos = escola_com_departamento.departamentos
print("A escola tem " + str(len(departamentos)) + ' departamentos');
escola_com_departamento.add_departamento(departamento_humanas)
print("Agora a escola tem " + str(len(departamentos)) + ' departamentos');