#kemalettin gui sınıfı
#aktas_1 ana pencere
#aktas_2 dosya nesnesi
#aktas_3 kıtaların geleceği küme
#kemalettin_2 dosya okurken kullanılan iteratör
#aktas_4 sıralama yapabilmek için kümedeki bilgilerin alındığı dizi
#aktas_5 kıtalar listbox için string değişken
#aktas_6 kıtalar listbox
#aktas_7 #kaydırma çubuğu
#aktas_8 ülkeler listbox için string değişken
#aktas_9 ülkeler listbox
#aktas_10 secilen kıtaya göre ülkeyi getiren metot
#aktas_11 kıta seçimi
#aktas_12 secilen kıtaya göre ülkeyi getiren metot

#aktas_13 seçilen kıtadan gelen ülkeler


from tkinter import *
class kemalettin: #gui için tanımlanan sınıf
    def __init__(self):
        self.aktas_1 = Tk() #ana pencere nesnesi
        self.aktas_1.title("DÜNYADAKİ KITALAR - ÜLKELER")
        Label(self.aktas_1, text = "KITALAR").grid(row=0, column=0)
        Label(self.aktas_1, text="ÜLKELER").grid(row=0,column=1)

        self.aktas_2 = open('dunya.txt','r') #dosya nesnesi
        self.aktas_3 = set()  #dosyadan gelecek kıtalar kümesi

        for kemalettin_2 in self.aktas_2:
            kemalettin_2 = kemalettin_2.split(",")[1]
            self.aktas_3.add(kemalettin_2)


        self.aktas_2.close()
        self.aktas_4 = list(self.aktas_3) #kümedeki bilgilerin liste hali sıralama yapabilmek için
        self.aktas_4.sort()

        self.aktas_5 = StringVar() # kıtalar listbox için string değişken
        self.aktas_6 = Listbox(self.aktas_1, width=9, height=len(self.aktas_4), listvariable=self.aktas_5) #kıtalar listbox
        self.aktas_6.grid(row=1, column=0, sticky=N)
        self.aktas_5.set(tuple(self.aktas_4))
        self.aktas_6.bind("<<ListboxSelect>>", self.aktas_10)
        self.aktas_7 = Scrollbar(self.aktas_1,orient=VERTICAL) #kaydırma çubuğu
        self.aktas_7.grid(row=1,column=2,sticky=NS)
        self.aktas_8 = StringVar() #ülkeler listbox için string değişken
        self.aktas_9 = Listbox(self.aktas_1, width=45, height=len(self.aktas_4), listvariable = self.aktas_8, yscrollcommand=self.aktas_7.set) # ülkeler listbox
        self.aktas_9.grid(row=1,column=1,sticky=NSEW)
        self.aktas_7["command"] = self.aktas_9.yview

        self.aktas_1.mainloop()

    def aktas_10(self,aktas_13):
        self.aktas_11 = self.aktas_6.get(self.aktas_6.curselection()) #kıta secimi
        self.aktas_12 = [i.split(',')[0] for i in open('dunya.txt','r') if i.split(',')[1].rstrip() == self.aktas_11] #seçilen kıtadan gelen ülkeler


kemalettin()