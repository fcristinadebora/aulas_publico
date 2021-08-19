class Multiplicacao:
     #Utilizo a notação @staticmethod para dizer que o método é estático
    @staticmethod
    def multiplicacao(vetor_valores):
        if (not isinstance(vetor_valores, list)):  # verifica se o parametro recbido é uma instancia de lista (vetor)
            print('O parametro deve ser um vetor')
            return  # retorna o método, usando o princípio de Early Return

        if (len(vetor_valores) < 2):  # Verifica se o tamanho do parametro é menor que 2
            print('O parametro deve ter pelo menos 2 valores')
            return  # retorna o método, usando o princípio de Early Return

        produto_total = None  # inicializa a variável que vai armazenar o produto total
        for valor in vetor_valores:  # itera (passa por) todos os valores de vetor_valores
            print('O valor atual é' + str(valor))
            if (produto_total is None):  # se a variável ainda não recebeu nenhum valor, irá ocorrer na primeira iteração
                produto_total = valor  # o novo valor da variável é o valor da primeira posição do vetor
                print("Primeira passagem no Loop, o produto total é " + str(produto_total))
                continue  # a instrução "continue" irá continuar o loop para a próxima posição, ignorando o restante das instruções, pois já fez o que deveria ser feito

            print('Agora já tem valor, vamos multiplicar')
            produto_total = produto_total * valor
            print('O novo produto total é ' + str(produto_total))

        return produto_total
