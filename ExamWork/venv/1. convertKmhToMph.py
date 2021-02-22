#kullanıcıdan km olarak alınan uzaklık bilgisi mile çevirilir
#mil=km*0,6214
#fonksiyon
def kmdenMile(mesafe):
    return mesafe*0.6124

def main():
    x=float(input("Kilometre cinsinden mesafe girin:"))
    print("{:0.2f} kilometre {:0.2f} mile eşittir".format(x,kmdenMile(x)))

main()