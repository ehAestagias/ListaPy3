def binario():
    global string_reversed
    global num
    global bin
    global rest

    while(num>0):
        resto = num % 2
        bin += str(resto)
        num = num//2
    i = len(bin)
    while i >0:
        string_reversed += bin[i-1]
        i = i-1
    print(string_reversed)

rest = 0
string_reversed = bin = ""
num = int(input())
binario()