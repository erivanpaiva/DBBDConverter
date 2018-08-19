#function DEC -> BIN
def decbin(num):
    num_f = float(num)
    num_i = int(num_f)
    tam = len(str(num_i))
    resto = (round(num_f % 1,3))
    total_i = ("")
    total_f = ("")
    if num.find(".") == -1:
        dec =  int(num)
        if num == "0":
            total_i = num
        else:
            while dec != 0:
                rest = int(dec%2)
                dec = int(dec/2)
                total_i += str(rest)
        return (total_i[::-1])
    else:
        total1 = 0
        total2 = 0.0
        if num_i == 0:
            total1 = str(num_i)
        else:
            while num_i != 0:
                rest = int(num_i%2)
                num_i = int(num_i/2)
                total_i += str(rest)
            total1 = str(total_i[::-1])
        while (resto != 1.0):
            resto = resto*2
            if int(resto) == 0:
                total_f += "0"
            elif int(resto) == 1:
                total_f += "1"
            else:
                total_f += "1"
                resto = resto % 1
            if(len(total_f) > 5):
                break
        total2 = str(total_f)
        return(total1+"."+total2)
    
#função BIN -> DEC
def bindec(num):
    num_f = float(num)
    b = str(int(num_f))
    b = (b[::-1])
    resto = str(round(num_f % 1,3))
    tam1 = len(num)
    tam2 = len(b)
    tam3 = len(str(resto))
    bin2 =(num[::-1])

    if num.find(".") == -1:
        x = 0
        total = 0
        for x in range(0, tam1):
            total += int(bin2[x]) * (2**x)
        return(total)
    else:
        x = 0
        y = 0
        neg = -1
        total2 = 0
        total3 = 0
        for x in range(0, tam2):
            total2 += int(b[x]) * (2**x)
        for y in range(2,tam3):
            total3 += (int(resto[y]) * (2**neg))
            neg = neg - 1
        return(total2+total3)

select = input("""--- CONVERSOR BÁSICO ---
O que gostaria de fazer?
1 - converter de decimal para binário
2 - converter de binário para decimal
""")
while (select != "1") & (select != "2"):
    select = input("ERRO | escolha entre 1 e 2: ")

if (select == '1'):
    num = input("digite um número: ")
    print ("DEC -> BIN | " + num + " -> " + (decbin(num)))
else:
    num = input("digite um número: ")
    print ("DEC -> BIN | " + num + " -> " + str((bindec(num))))
