#Bir ilçe, mülkün gerçek değerinin yüzde 60'ı olan mülkün değerlendirme değeri üzerinden
# emlak vergileri toplar. Örneğin, bir dönüm arazi 10.000 ABD Doları değerindeyse,
# değerlendirme değeri 6.000 ABD Dolarıdır. Bu durumda emlak vergisi, değerlendirme
# değerinin her 100 $ 'ı için 72 ¢' dir. 6.000 $ olarak belirlenen dönüm için vergi 43.20 $
# olacaktır. Bir mülkün gerçek değerini soran ve değerlendirme değerini ve emlak vergisini
# gösteren bir program yazın.

def emlakVergisi(gercekdeger):
    degerlendirme_degeri=gercekdeger*0.6
    vergi=degerlendirme_degeri/100*0.72
    return degerlendirme_degeri,vergi

def main():
    mulk=int(input("Mülkünüzün piyasa değerini girin:"))
    matrah, tahakkuk=emlakVergisi(mulk)
    print("Mülkünüzün vergi matrahı {:0.2f} TL, "
          "tahakkuk eden emlak vergisi {:0.2f} TL'dir".format(matrah,tahakkuk))

main()