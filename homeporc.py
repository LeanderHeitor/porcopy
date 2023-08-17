from json import dumps, loads
import os
#mostrar todos os arquivos .txt de uma pasta
def ListaDeArquivos():
    arquivos = os.listdir()
    arquivos_txt = (arquivo for arquivo in arquivos if arquivo.endswith('.txt'))
    ArquivoSemExtensao = (os.path.splitext(arquivo)[0] for arquivo in arquivos_txt)
    return ArquivoSemExtensao

def AdicionarPorcos():
    idade = int(input("Digite a idade do seu animal: "))
    sexo = input("Digite o sexo do seu animal: ")
    raca = input("Digite a raça do seu animal: ")
    pes = int(input("Digite o peso do seu animal(Kg): "))
    racaoDia = int(input("Digite a quantidade de ração que o seu animal come por dia: "))
    vacina = list()
    op = input("O seu animal já tomou vacina?\n1. Sim\n2. Não\nEscolha uma opção: ")
    if op == '1': #caso o animal já tenha tomado vacina, o usuário informa o nome da vacina e a quantidade de vacinas que o animal tomou
        ask = int(input("Quantas vacinas o seu animal tomou?\n"))
        for i in range(ask):
            vacina.append(input("Digite o nome da vacina: "))
        por[nom] = {'Idade': idade, 'Sexo': sexo, 'Raça': raca, 'Peso': pes, 'Ração por dia': racaoDia, 'Vacinas': vacina} #adiciona os dados do porco no dicionário
        return por

    elif op == '2': #caso o animal não tenha tomado vacina, o valor da chave Vacinas é vazio
        por[nom] = {'Idade': idade, 'Sexo': sexo, 'Raça': raca, 'Peso': pes, 'Ração por dia': racaoDia, 'Vacinas': []} #adiciona os dados do porco no dicionário
        return por
    else:
        print("Opção inválida")

#menu principal
while True:
    ArquivoSemExtensao = list(ListaDeArquivos())
    ordem = len(ArquivoSemExtensao)
    for i,nome in enumerate(ArquivoSemExtensao, start=1):
        print(f'{i}. {nome}')
    print(f'{ordem+1}. Adicionar baia')
    print(f'0. Sair')
    ask = input("Escolha uma das opções: ")

    #lista de numeros de 0 até o numero de arquivos + 1
    lista = list(range(1,ordem+1))

    #dicionário com os numeros da lista e os nomes dos arquivos
    dicionario = dict(zip(lista, ArquivoSemExtensao))

    #verifica se a opção escolhida está na lista
    if int(ask) in lista:
        baiaAberta = dicionario[int(ask)]
        arquivo = str(baiaAberta)
    
        f = open(f'{arquivo}.txt', 'r')
        if f.read() == '': #verifica se o arquivo está vazio
            por = dict()
            while True:
                print(f'1. Adicionar porco')
                print(f'0. Sair')
                ask = input("Escolha uma das opções: ")
                if ask == '1':
                    nom = input("Digite o nome do seu animal: ")
                    por = AdicionarPorcos()
                    f = open(f'{arquivo}.txt', 'w')
                    f.write(dumps(por))
                    f.close()
                    break
                elif ask == '0':
                    break
                else:
                    print("Opção inválida")
        else:
            f = open(f'{arquivo}.txt', 'r')
            por_disserializado = loads(f.read())
            f.close()   
            #menu secundário para adicionar, verificar ou remover porcos
            while True:
                f = open(f'{arquivo}.txt', 'r')
                por_disserializado = loads(f.read())
                f.close()
                x = len(por_disserializado)+1
                for i,porco in enumerate(por_disserializado, start=1): #mostra os porcos da baia
                    print(f'{i}. {porco}')
                print(f'{len(por_disserializado)+1}. Adicionar porco')
                print(f'{len(por_disserializado)+2}. Remover baia')
                print(f'0. Sair')

                ask = input("Escolha uma das opções: ")

                #lista de numeros de 0 até o numero de porcos + 1
                lista = list(range(1,len(por_disserializado)+1))

                #dicionário com os numeros da lista e os nomes dos porcos
                dicionarioPorcos = dict(zip(lista, por_disserializado))

                #verifica se a opção escolhida está na lista
                if int(ask) in lista:
                    porcoAberto = dicionarioPorcos[int(ask)]
                    print(f'Identificação: {porco}')
                    print(f"Idade: {por_disserializado[porco]['Idade']}")
                    print(f"Sexo: {por_disserializado[porco]['Sexo']}")
                    print(f"Raça: {por_disserializado[porco]['Raça']}")
                    print(f"Peso: {por_disserializado[porco]['Peso']}")
                    print(f"Ração por dia: {por_disserializado[porco]['Ração por dia']}")
                    lista = ' ,'.join(por_disserializado[porco]['Vacinas'])
                    print(f"Vacinas: {lista}")

                    print('1. Atualizar dados')
                    print('2. Remover porco')
                    print('0. Sair')
                    ask = input("Escolha uma das opções: ")
                    if ask == '1':
                        f = open(f'{arquivo}.txt', 'r')
                        por_disserializado = loads(f.read())
                        ask = input('''Qual dado deseja atualizar?
                                                1. Idade
                                                2. Peso
                                                3. Ração por dia
                                                4. Vacinas
                                                Escolha uma opção: ''')
                        if ask == '1':
                                        por_disserializado[porcoAberto]['Idade'] = int(input("Digite a nova idade: "))
                                        f = open(f'{arquivo}.txt', 'w')
                                        f.write(dumps(por_disserializado))
                                        f.close()
                        elif ask == '2': 
                                        por_disserializado[porco]['Peso'] = input("Digite o novo peso: ")
                                        f = open(f'{arquivo}.txt', 'w')
                                        f.write(dumps(por_disserializado))
                                        f.close()
                        elif ask == '3':
                                        por_disserializado[porco]['Ração por dia'] = input("Digite a nova quantidade de ração por dia: ")
                                        f = open(f'{arquivo}.txt', 'w')
                                        f.write(dumps(por_disserializado))
                                        f.close()
                        elif ask == '4':
                                        ask = input("Qual vacina deseja adicionar?\n")
                                        por_disserializado[porcoAberto]['Vacinas'].append(ask) #adiciona a vacina na lista de vacinas
                                        f = open(f'{arquivo}.txt', 'w')
                                        f.write(dumps(por_disserializado)) #serializa os dados do arquivo e escreve no arquivo
                                        f.close()
                                    
                        else:
                                        print("Opção inválida!")
                    elif ask == '2':
                        f = open(f'{arquivo}.txt', 'r')
                        por_disserializado = loads(f.read())
                        f.close()
                        del por_disserializado[porcoAberto]
                        f = open(f'{arquivo}.txt', 'w')
                        f.write(dumps(por_disserializado))
                        print('Porco removido com sucesso!')
                
                elif ask == str(len(por_disserializado)+1): #adiciona um porco
                    por = {}
                    nom = input("Digite uma identificação para o animal: ")
                    if nom in por_disserializado:
                        print('Identificação já cadastrada!')
                        break
                    else:
                        por = AdicionarPorcos()

                        f = open(f'{arquivo}.txt', 'r')
                        if f.read() == '': #verifica se o arquivo está vazio
                            f.close()
                            f = open(f'{arquivo}.txt', 'w')
                            f.write(dumps(por))
                        else:
                            f.close
                            f = open(f'{arquivo}.txt', 'r')
                            por_disserializado = loads(f.read()) #caso não esteja vazio, carrega os dados do arquivo
                            f.close()
                            por_disserializado.update(por) #adiciona os dados do porco no dicionário
                            f = open(f'{arquivo}.txt', 'w')
                            por_disserializado = dumps(por_disserializado) #serializa os dados do arquivo
                            f.write(por_disserializado) #escreve os dados no arquivo
                        f.close()
                elif ask == str(len(por_disserializado)+2):
                    f = open(f'{arquivo}.txt', 'r')
                    f.close()
                    os.remove(f'{arquivo}.txt') #remove o arquivo
                    print("Baia removida com sucesso!")
                    break
                elif ask == '0':
                    break
                else:
                    print("Opção inválida!")
    #adiciona baia
    elif ask == str(ordem+1):
        print(f'''1. Adicionar baia
              2. Voltar ao Menu Principal''')
        ask = input("Escolha uma das opções: ")
        if ask == '1':
            nome = input('Adicione o nome da baia:')
            try:
                with open(f'{nome}.txt', 'x') as file: #verifica se arquivo como nome da baia já existe
                    print("Baia cadastrada com sucesso!")
            except FileExistsError: 
                print("Baia já cadastrada!") #caso exista, retorna mensagem de erro

    elif ask == '0':
        break
