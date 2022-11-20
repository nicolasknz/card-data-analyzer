from dados import dados as dados_brutos

try:
    colunas = ['marca', 'modelo', 'combustivel', 'cilindros', 'tipo',
               'potencia', 'peso', 'consumo_cidade', 'consumo_estrada', 'preco']
    dados = []

    escolha = input('''Selecione uma opção:
    1. Apresentação do desvio padrão de uma coluna específica
    2. Apresentação dos veículos ordenados segundo uma das colunas específica
    3. Apresentação dos 5 veículos com os maiores valores de uma coluna específica
    4. Apresentação dos 5 veículos com os menores valores de uma coluna específica
    5. Apresentação da quantidade de carros para cada tipo de valor de uma coluna específica
    6. Exibir os todos os dados de um veículo fornecendo o nome do modelo

    Sua escolha -> ''')
    escolha = int(escolha)

    print('')
    print('')

    def tamanho_lista(lista):
        tamanho = 0
        for i in lista:
            tamanho += 1
        return tamanho

    def somar_lista(lista):
        soma = 0
        for i in lista:
            soma += i
        return soma

    # Transforma os dados brutos em uma lista de dicionários para facilitar a manipulação
    for i in range(tamanho_lista(dados_brutos)):
        dicionario = {}
        for k in range(tamanho_lista(colunas)):
            dicionario[colunas[k]] = dados_brutos[i][k]
        dados.append(dicionario)

    def inverter_lista(lista):
        lista_invertida = []
        for i in range(tamanho_lista(lista)):
            lista_invertida.append(lista[tamanho_lista(lista) - 1 - i])
        return lista_invertida

    def bubble_sort_por_coluna(lista, coluna):
        for i in range(tamanho_lista(lista)):
            for j in range(tamanho_lista(lista) - 1):
                if lista[j][coluna] > lista[j + 1][coluna]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

    def desvio_padrao(lista, coluna):
        valores = [valor[coluna] for valor in lista]
        print(valores)
        media = somar_lista(valores) / tamanho_lista(valores)
        variancia = somar_lista(
            [(x - media) ** 2 for x in valores]) / tamanho_lista(valores)
        resultado = variancia ** 0.5
        return ['Desvio padrao por consumo na cidade', resultado]

    def ordenar(lista, coluna):
        lista_ordenada = bubble_sort_por_coluna(lista, coluna)

        resposta = [
            f'{item["marca"]} {item["modelo"]} -> {item["preco"]}'for item in lista_ordenada]

        return ['Carros ordenados por preco', *resposta]

    def ordernar_cinco_maiores(lista, coluna):
        lista_ordenada = bubble_sort_por_coluna(lista, coluna)
        lista_ordenada = inverter_lista(lista_ordenada)
        cinco_maiores = [
            f'{item["marca"]} {item["modelo"]} -> {item[coluna]}'for item in lista_ordenada[:5]
        ]

        return ["Cinco carros mais potentes", *cinco_maiores]

    def ordenar_cinco_menores(lista, coluna):
        lista_ordenada = bubble_sort_por_coluna(lista, coluna)
        cinco_menores = [
            f'{item["marca"]} {item["modelo"]} -> {item[coluna]}'for item in lista_ordenada[:5]]

        return ['Cinco carros com menor consumo na estrada', *cinco_menores]

    def quantidade_por_tipo(lista, coluna):
        valores = [valor[coluna] for valor in lista]
        resposta = {}
        for valor in valores:
            if valor in resposta:
                resposta[valor] += 1
            else:
                resposta[valor] = 1
        return ['Quantidade de carros pelo estilo', resposta]

    def dados_por_modelo(lista, coluna):
        modelo = input('Digite o modelo: ')

        for item in lista:
            if item[coluna] == modelo:
                return ['Dados do carro pelo modelo', item]
        return ['Dados do carro pelo modelo', 'Modelo não encontrado']

    # dicionario que mapeia as funções de acordo com a escolha do usuário
    de_escolha_para_funcao = {
        1: {
            'coluna': 'consumo_cidade',
            'funcao': desvio_padrao,
        },
        2: {
            'coluna': 'preco',
            'funcao': ordenar,
        },
        3: {
            'coluna': 'potencia',
            'funcao': ordernar_cinco_maiores,
        },
        4: {
            'coluna': 'consumo_estrada',
            'funcao': ordenar_cinco_menores,
        },
        5: {
            'coluna': 'tipo',
            'funcao': quantidade_por_tipo,
        },
        6: {
            'coluna': 'modelo',
            'funcao': dados_por_modelo,
        }
    }

    # Mecanismo que define qual função será executada e qual coluna será usada baseada no input do usuário
    coluna = de_escolha_para_funcao[escolha]['coluna']
    funcao = de_escolha_para_funcao[escolha]['funcao']
    resposta = funcao(dados, coluna)

    print('---------------------------------------------')
    print(*resposta, sep='\n')
    print('---------------------------------------------')
except:
    print('---------------------------------------------')
    print('Comando nao encontrado!')
    print('---------------------------------------------')
