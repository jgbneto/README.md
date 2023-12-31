n1 = '1. Adicionar registro de estudante'
n2 = '2. Exibir registro de estudante'
n3 = '3. Procurar por um estudante'
n4 = '4. Calcular média das notas'
n5 = '5. Salvar registros em arquivo'
n6 = '6. Carregar registros de arquivo'
n7 = '7. Sair'

estudantes = []

while True:
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    print(n6)
    print(n7)

    escolha = input('Digite sua escolha (1-7): ')

    if escolha == '1':
        nome = input('Digite o nome do estudante: ')
        id_estudante = input('Digite o ID do estudante: ')
        notas = input('Digite as notas do estudante (separadas por espaço): ').split()
        notas = [float(nota) for nota in notas]
        estudante = {"Nome": nome, "ID": id_estudante, "Notas": notas}
        estudantes.append(estudante)

    elif escolha == '2':
        if estudantes:
            for estudante in estudantes:
                print(f"Nome: {estudante['Nome']}")
                print(f"ID: {estudante['ID']}")
                print(f"Notas: {', '.join(map(str, estudante['Notas']))}")
        else:
            print('Nenhum registro de estudante encontrado.')

    elif escolha == '3':
        id_procurado = input('Digite o ID do estudante a ser procurado: ')
        for estudante in estudantes:
            if estudante["ID"] == id_procurado:
                print("Estudante encontrado:")
                print(f"Nome: {estudante['Nome']}")
                print(f"ID: {estudante['ID']}")
                print(f"Notas: {', '.join(map(str, estudante['Notas']))}")
                break
        else:
            print(f"Nenhum estudante com ID {id_procurado} encontrado.")

    elif escolha == '4':
        if estudantes:
            notas_totais = sum([sum(estudante['Notas']) for estudante in estudantes])
            quantidade_estudantes = len(estudantes)
            media = notas_totais / quantidade_estudantes
            print(f'Média das notas de todos os estudantes: {media:.2f}')
        else:
            print('Nenhum registro de estudante encontrado.')

    elif escolha == '5':
        nome_arquivo = input('Digite o nome do arquivo para salvar os registros: ')
        with open(nome_arquivo, 'w') as arquivo:
            for estudante in estudantes:
                linha = f"{estudante['Nome']},{estudante['ID']},{','.join(map(str, estudante['Notas']))}\n"
                arquivo.write(linha)
        print(f'Registros salvos em {nome_arquivo}')

    elif escolha == '6':
        nome_arquivo = input('Digite o nome do arquivo para carregar os registros: ')
        estudantes = []
        try:
            with open(nome_arquivo, 'w') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    dados = linha.strip().split(',')
                    nome = dados[0]
                    id_estudante = dados[1]
                    notas = list(map(float, dados[2].split(',')))
                    estudante = {"Nome": nome, "ID": id_estudante, "Notas": notas}
                    estudantes.append(estudante)
            print(f'Registros carregados de {nome_arquivo}')
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando nova lista de estudantes vazia.")
            estudantes = []

    elif escolha == '7':
        print('Até logo!')
        break

    else:
        print('Escolha inválida. Digite um número de 1 a 7.')
