#Program eyalet ve ilçe satış vergisini hesaplamalıdır.
# devlet satış vergisinin yüzde 5, ilçe satış vergisinin ise yüzde 2,5 olduğunu varsayalım.
# Program, satın alma tutarını, devlet satış vergisini, ilçe satış vergisini, toplam satış
# vergisini ve satış toplamını (satınalma tutarının toplamı ile toplam satış vergisinin
# toplamıdır) göstermelidir. Kullanıcıdan satış fiyatı alınacak

def vergiHesapla(fiyat):
    devlet=fiyat*0.05
    ilce=fiyat*0.025
    toplam=fiyat+ilce+devlet
    return devlet,ilce,toplam
def main():
    satisfiyatı=int(input("Satış fiyatını girin:"))
    devletvergisi,ilceverigisi,top=vergiHesapla(satisfiyatı)
    print("Satış Fiyatı\tDevlet Vergisi\tİlçe Vergisi Toplam ")
    print(str(satisfiyatı),"\t\t\t\t",str(devletvergisi),"\t\t",str(ilceverigisi),"\t\t",str(top))
main()
