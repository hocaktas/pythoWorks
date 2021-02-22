#Pek çok finans uzmanı, mülk sahiplerinin evlerini veya binalarını, yapıyı değiştirmenin
# maliyetinin en az yüzde 80'i için sigortalamaları gerektiğini tavsiye ediyor.
# Kullanıcıdan bir binanın yenileme maliyetini girmesini isteyen ve ardından
# mülk için satın alması gereken minimum sigorta miktarını gösteren bir program yazın

def sigortaTutari(yenilemeMaliyeti):
    return yenilemeMaliyeti*0.8

def main():
    yenileme=int(input("Evinizin yenileme maliyetini girin:"))
    print("Evinizin en az {:0.2f} tutarınını sigortalamanız tavsiye edilir.".format(sigortaTutari(yenileme)))

main()