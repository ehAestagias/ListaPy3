# a soma de todas as areas ja é a area do imovel
def casa(infos):
    area = 1
    areatotal = 0
    for x in range(0,len(infos)):
        area = infos[x][1] * infos[x][2]
        areatotal = areatotal + area
        print(f'comodo: {infos[x][0]} -- area: {area}')
        print(f'area total: {areatotal}')
comodos = []
dados = []
qtd = int(input('quantos comodos tem a casa? '))
for x in range(0,qtd):
    dados.append(input('nome do comodo: '))
    dados.append(int(input('largura do comodo: ')))
    dados.append(int(input('comprimento do comodo: ')))
    comodos.append(dados[:])
    dados.clear()
casa(comodos)