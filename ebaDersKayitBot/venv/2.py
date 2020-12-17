dosya=open("k.txt","r",encoding='utf-8')
derslistesi=list
for satir in dosya:
    satir=satir.split(";")
    print(satir)

