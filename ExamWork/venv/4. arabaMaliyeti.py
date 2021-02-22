#Kullanıcıdan, otomobilini kullanmaktan kaynaklanan aşağıdaki masraflar için
# aylık maliyetleri girmesini isteyen bir program yazın: kredi ödemesi, sigorta, gaz, yağ,
# lastikler ve bakım. Program daha sonra bu giderlerin toplam aylık maliyetini ve
# bu harcamaların toplam yıllık maliyetini göstermelidir.

def MaliyetBul(kredi,sigorta,gaz,yag,lastik,bakim):
    aylikTop=kredi+sigorta+gaz+yag+lastik+bakim
    yillikTop=aylikTop*12
    return aylikTop,yillikTop

def main():
    aylik, yillik=MaliyetBul(int(input("Kredi ödemesi:")),
                               int(input("Sigorta ödemesi:")),
                               int(input("Gaz harcaması:")),
                               int(input("Gaz harcaması:")),
                               int(input("Lastik harcaması:")),
                               int(input("Bakim harcaması:"))
                               )
    print("Aylık araba harcamaları {:0.2f} TL, yıllık maliyetiniz {:0.2f}TLdir".format(aylik,yillik))

main()