#tem q ver de arrumar o max e o min ou fazer do outro jeito
def maiormenor(dados):
    maior = max(dados)
    menor = min(dados)
    print(maior)
    for x in range(0,len(dados)):
        if(dados[x] == maior):
            print(f'maior numero: {maior} posição: {x}')
        if(dados[x] == menor):
            print(f'maior numero: {menor} posição: {x}')

numeros = []
qtd = int(input('quantos numeros deseja adicionar a lista: '))
for x in range(0,qtd):
    num = int(input('digite um numero: '))
    while(numeros.count(num)==True):
        num = int(input('digite outro numero numero: '))
    numeros.append(num)
maiormenor(numeros)