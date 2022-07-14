def primo():
    global cont
    global num
    for x in range(1,num):
        if(num%x==0):
            cont = cont + 1
    if(cont>2):
        print('numero nao primo')
    else:
        print('numero primo')
cont = 0
num = int(input('digite um numero: '))
primo()