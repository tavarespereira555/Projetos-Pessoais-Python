from Tratamento_de_Erros.Modulos_115.Def_115 import titulo, nomes
while True:
    titulo('Menu Principal')
    print('1 - \033[34mVer pessoas cadastradas\033[m')
    print('2 - \033[34mCadastar pessoas novas\033[m')
    print('3 - \033[34mSair do sistema\033[m')
    resp= int(input('Sua Opcao: '))
    match resp:
        case 1:
            titulo('Pessoas Cadastradas')
            for i in range(0,len(nomes),2):
                print(f'{nomes[i]:<30}  {nomes[i + 1]} anos')
        case 2 :
            titulo('Novo Cadastro')
            n1= str(input('Nome: '))
            nomes.append(n1)
            while True:
                try:
                    idade=int(input('Idade: '))
                except ValueError:
                    print('\033[31mERRO!!! Digite apenas numero inteiro validos\033[m')
                    continue
                else:
                    nomes.append(idade)
                    break

            print(f'Novo registro de {n1} adicionado')
        case 3:
            titulo('Saindo do sistema... Volte Sempre!!')
            break
        case _:
            print('Opção inválida!')