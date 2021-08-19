class Mes:
    # Atributos da classe
    JANEIRO = {'numero': '01', 'nome': 'Janeiro'}
    FEVEREIRO = {'numero': '02', 'nome': 'Fevereiro'}
    MARCO = {'numero': '03', 'nome': 'Março'}
    ABRIL = {'numero': '04', 'nome': 'Abril'}
    MAIO = {'numero': '05', 'nome': 'Maio'}
    JUNHO = {'numero': '06', 'nome': 'Junho'}
    JULHO = {'numero': '07', 'nome': 'Julho'}
    AGOSTO = {'numero': '08', 'nome': 'Agosto'}
    SETEMBRO = {'numero': '09', 'nome': 'Setembro'}
    OUTUBRO = {'numero': '10', 'nome': 'Outubro'}
    NOVEMBRO = {'numero': '11', 'nome': 'Novembro'}
    DEZEMBRO = {'numero': '12', 'nome': 'dezembro'}

    # Método estático usando decorator @staticmethod
    @staticmethod
    def get_lista_meses():
        return [
            Mes.JANEIRO,
            Mes.FEVEREIRO,
            Mes.MARCO,
            Mes.ABRIL,
            Mes.MAIO,
            Mes.JUNHO,
            Mes.JULHO,
            Mes.AGOSTO,
            Mes.SETEMBRO,
            Mes.OUTUBRO,
            Mes.NOVEMBRO,
            Mes.DEZEMBRO
        ]
