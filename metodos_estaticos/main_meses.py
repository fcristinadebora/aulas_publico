from classes.mes import Mes

meses = Mes.get_lista_meses()

for mes in meses:
    print(str(mes['numero']) + ' - ' + mes['nome'])