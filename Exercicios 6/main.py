def calcula_probabilidade(pessoas):
    ci = (1.0/365)**pessoas
    for i in range((366-pessoas),366):
        ci *= i
    ci = 1-ci
    cii = ci * 100
    p = round(cii,2)

    if(p == 80):
        print('Existem 80 por cento de chance de duas pessoas na sala fazerem aniversário no mesmo dia.')
    elif(p > 80):
        if(p > 100):
            p = 100
        print('Existem mais de 80 por cento de chance de duas pessoas na sala fazerem aniversário no mesmo dia.')
        print(f'São {p}% de chance numa sala com {pessoas} pessoas.')
    else:
        print('Existem menos de 80 por cento de chance de duas pessoas na sala fazerem aniversário no mesmo dia.')
        print(f'São {p}% de chance numa sala com {pessoas} pessoas.')

    

n_pessoas = int(input('Quantas pessoas tem na sala? '))

calcula_probabilidade(n_pessoas)

