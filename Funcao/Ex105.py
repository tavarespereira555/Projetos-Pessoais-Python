def notas(* num, sit=False):
    """
    -> Funcao para avaliar notas e situacoes de vários alunos
    :param num: um ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não mostrar situação
    :return: dicionario com várias informacoes sobre a situacao da turma
    """
    diciona= dict()
    mai = meno  = 0
    pos= 0
    m= 0
    soma= 0
    while pos < len(num):
        if pos == 0:
            mai =num[pos]
        else:
            if num[pos] > mai:
                mai= num[pos]
        pos +=1
    pos1= 0
    while pos1 < len(num):
        if pos1 == 0:
            meno= num[pos1]
        else:
            if num[pos1] < meno:
                meno= num[pos1]
        pos1 +=1
    pos2= 0
    while pos2 < len(num):
        soma += num[pos2]
        pos2 += 1
    m= soma / len(num)
    if sit:
        if m > 7:
            diciona['sit']= 'Boa'
        elif m < 4:
            diciona['sit']= 'Ruim'
        else:
            diciona['sit']= 'Razoável'
    diciona['Quanti'] = len(num)
    diciona['Maior'] = mai
    diciona['Menor']= meno
    diciona['Media']= m
    return diciona


print(notas(10,5,5,10,8))
