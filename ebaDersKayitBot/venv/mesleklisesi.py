#EĞER İLGİLİ DERSİN EK KATILIMCISI YOKSA İLGİLİ KISMA 0 YAZILACAK, DERSİN SADECE ÜNİTESİ VAR KONUSU YOKSA KONU YERİNE 0 YAZILACAK( ESKİ MODÜLLER İÇİN)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
tc="17980037094"#input("E-devlet için Tc Kimlik girin:")
passw="06et0370"#input("E-devlet için şifre girin:")
driver = webdriver.Chrome('C:\\Users\\Kemalettin\\Downloads\\chromedriver.exe')

def Main():
       try:
              dosya = open("kdersler.txt", "r",encoding="utf-8")
       except FileExistsError:
              print("Dosya bulunamadı")
       except:
              print("Dosya açmada hata oluştu")

       sayfa_ac(url="http://www.eba.gov.tr/#/anasayfa")
       edevlet_giris(tc=tc,parola=passw)


       canli_ders()
       for satir in dosya:
              if "$" in satir:
                     break;
              satir = satir.split(";")
              ders_bilgileri_gir(dersbaslik=satir[0].capitalize(),
                                 sinif=satir[1],
                                 sube=satir[2],
                                 dersgunu=satir[3].strip(),
                                 derssaati=satir[4].strip(),
                                 dersuygulamasi=satir[5].capitalize(),
                                 derslinki=satir[6],
                                 dersparola=satir[7],
                                 dersadi=satir[8],
                                 unite=satir[9],
                                 konu=satir[10],
                                 katilimci=satir[11].upper()
                                 )
              print("Ayın {0}.günü saat {1}deki {2} dersi sisteme kaydedildi.".format(satir[3],satir[4],satir[8]))
              harici()

def sayfa_ac(url):
       driver.get("http://www.eba.gov.tr/#/anasayfa")

def edevlet_giris(tc,parola):

       ogrt_buton=driver.find_element_by_xpath("/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[3]")
       ogrt_buton.click()
       time.sleep(1)
       edevlet_buton=driver.find_element_by_xpath("//*[@id='teacher']/div/button[2]")
       edevlet_buton.click()
       time.sleep(1)
       tckimliktxt=driver.find_element_by_xpath("//*[@id='tridField']")
       parolatxt=driver.find_element_by_xpath("//*[@id='egpField']")

       tckimliktxt.send_keys(tc)
       parolatxt.send_keys(parola)
       if len(tc)!=11 or tc.isdigit()==False:
              print("Tc No'da yanlışlık var, dosyadan düzeltin")
              return
       time.sleep(1)
       girisbuton=driver.find_element_by_xpath("//*[@id='loginForm']/div[2]/input[4]")
       girisbuton.click()
       time.sleep(5)

def canli_ders():
       canliders=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/a/div")
       canliders.click()
       time.sleep(8)
       driver.find_element_by_link_text("TAMAM").click()
       time.sleep(3)

       harici="/html/body/div[1]/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div/div[2]"
       driver.find_element_by_xpath(harici).click()
       time.sleep(5)
       haricieklebtn="//*[@id='liveLessonList']/div[2]/div/div[2]/div/button"
       driver.find_element_by_xpath(haricieklebtn).click()
       time.sleep(3)
def harici():
       haricieklebtn="//*[@id='liveLessonList']/div[2]/div/div[2]/div/button"
       driver.find_element_by_xpath(haricieklebtn).click()
       time.sleep(3)


def ders_bilgileri_gir(dersbaslik,sinif,dersgunu,derssaati,derslinki,dersparola,dersadi,unite,sube,katilimci,dersuygulamasi,konu):
       dersbasliktxt="//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/input"
       driver.find_element_by_xpath(dersbasliktxt).send_keys(dersbaslik)
       time.sleep(2)

       snf_opt = driver.find_element_by_xpath("//select[@name='grade']")
       all_snf = snf_opt.find_elements_by_tag_name("option")
       for snf in all_snf:
              if sinif in str(snf.text):
                     snf.click()
                     break
       time.sleep(3)
       derstarihibtn="//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[1]/div[2]/div[3]/p/span/button"
       driver.find_element_by_xpath(derstarihibtn).click()
       gun="//td/button[span={g}]/span".format(g=int(dersgunu))
       gunspan=driver.find_element_by_xpath(gun)
       gunspan.click()
       time.sleep(2)

       select = Select(driver.find_element_by_name('endtime'))
       time.sleep(1)
       select.select_by_visible_text(derssaati)
       time.sleep(1)
       uyg = Select(driver.find_element_by_name('lessonType'))
       time.sleep(1)
       uyg.select_by_visible_text(dersuygulamasi)
       time.sleep(1)

       driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[7]/input").send_keys(derslinki)
       time.sleep(1)
       driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[8]/input").send_keys(dersparola)

       driver.find_element_by_xpath("//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]").click()
       driver.find_element_by_xpath("//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input[1]").send_keys(dersadi)
       time.sleep(1)
       driver.find_element_by_xpath("//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input[1]").send_keys(Keys.ENTER)
       time.sleep(2)
       unitesec="//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/select"
       u=Select(driver.find_element_by_xpath(unitesec))
       time.sleep(2)
       u.select_by_visible_text(unite)
       time.sleep(1)

       if konu!="0":
              konusec = '//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/select'
              k=Select(driver.find_element_by_xpath(konusec))
              time.sleep(2)
              k.select_by_visible_text(konu)
       time.sleep(2)
       driver.find_element_by_xpath("//*[@id='ebaEtudEditView']/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/span/button").click()

       time.sleep(3)
       subeler=driver.find_element_by_class_name("checkBoxContainer").find_elements_by_tag_name("label")
       for s in subeler:
              if sube in s.text[17:20]:
                     s.click()
       time.sleep(1)
       driver.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div').click()
       time.sleep(3)


       #katılımcı ekle 1 tane
       if katilimci.strip()!="0": #buradaki sorun çözülecek ve birden fazla katılımcı öğretmen eklenecek
              driver.find_element_by_xpath('//*[@id="assistantTeachersMultiSelect"]/span/button').click()
              time.sleep(2)
              driver.find_element_by_xpath('//*[@id="assistantTeachersMultiSelect"]/span/div/div[1]/div[2]/input').send_keys(katilimci)
              time.sleep(1)
              driver.find_element_by_xpath('//*[@id="assistantTeachersMultiSelect"]/span/div/div[2]/div').click()
              time.sleep(2)
       #ders kaydetme
       driver.find_element_by_xpath('//*[@id="ebaEtudEditView"]/div[2]/div/div/div[2]/div[2]/div[2]/div').click()
       time.sleep(2)
       driver.find_element_by_xpath('// *[ @ id = "ng-app"] / body / div[1] / div / div / div[3] / a').click()

Main()