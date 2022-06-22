def binario(x):
    global string_reversed
    global bin
    while(x>0):
        resto = x % 2
        bin += str(resto)
        x = x//2
    i = len(bin)
    while i >0:
        string_reversed += bin[i-1]
        i = i-1
    print(string_reversed)

string_reversed = bin = ""
num = int(input())
binario(num)