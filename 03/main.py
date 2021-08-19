from classes.pessoa import Pessoa
from classes.pessoaFisica import PessoaFisica
from classes.pessoaJuridica import PessoaJuridica

pessoa = Pessoa("João", "Concórdia") # uma classe pai também pode ser instanciada, normalmente
pessoaFisica = PessoaFisica("Debora", "Concórdia", "999.999.999-99", "23/10/1997")
pessoaJuridica = PessoaJuridica("Compufour Software LTDA", "Concórdia", "70.892.036/0001-02", "Compufour")

pessoa.imprimir_detalhes()
print('___________')
pessoaFisica.imprimir_detalhes()
print('___________')
pessoaJuridica.imprimir_detalhes()
print('___________')

print('Testando método reaproveitado da classe mãe')
pessoa.comprar('Computador')
pessoaFisica.comprar("Celular", 1)
pessoaJuridica.comprar("Monitor")

