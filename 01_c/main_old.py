from classes.multiplicacao import Multiplicacao

vetor = [2, 3, 4]
# Executando o método de forma estática
produto_total = Multiplicacao.multiplicacao(vetor)

# Instanciando um novo objeto
multiplicacao_obj = Multiplicacao()
# Executando o método de forma não estática
produto_total = multiplicacao_obj.multiplicacao(vetor)

print('O produto total do vetor é = ' + str(produto_total))