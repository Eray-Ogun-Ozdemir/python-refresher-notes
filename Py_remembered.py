#%% Liste
meyveler = ["Elma","Armut","Karpuz","Kavun"]

print(meyveler)

len(meyveler)

#Eleman ekleme
meyveler.append("Muz")

#Belirli bir index'e veri ekleme
meyveler.insert(0, "Çilek")

#Güncelleme
meyveler[2] = "Kiraz"

#Veri silme
meyveler.pop()

meyveler.pop(0)

#Seçme
#meyveler[6]

meyveler[-1]

meyveler[0:3]
#%% Tuple
veritabani = ("Localhost","admin",123456)

sayilar = (1,2,3)

veritabani.count("admin") #elemanı 

len(veritabani)
#%% Set
set1 = {1,2,3,4,5,5,5,5,5,5,5}
list2 = [1,2,3,4,5,5,5,5,5,5,5]

set2 = set(list2)
print(set2)

set3 = {1,2,3}
set4 = {3,4}

print(set3.difference(set4))
print(set4.difference(set3))

print(set4.intersection(set3))
#%% dictionary

kisi = {
        "Ad":"Eray Ogün",
        "Soyad":"Özdemir",
        "Yas":24
        }

personeller = {
    "Ad":["Eray","Ogün","Birgül"],
    "Şehir":["Düzce","Sinop","Bolu","İstanbul"]
    }

personeller["Yaş"] = 30

personeller["Yaş"] = [30,25,28]

print(personeller.get("Maaş","There is no column like that"))
# End of data types
#%% Fonksiyonlar

# Python'da kod tekrarını önler

# Parametresiz fonk
def hello():
    print("hello")
    
hello()

# Parametreli fonk
def hello_name(name = "Admin"):
    print("hello,",name)

hello_name("Eray")

hello_name()

# Birden fazla parametreli fonk
def maas_hesapla(brut_maas,vergi_orani):
    #print("Net maaşınız : ", brut_maas*(1-vergi_orani))
    #return brut_maas*(1-vergi_orani)
    net_maas = brut_maas*(1-vergi_orani)
    return net_maas

maas_hesapla(100,0.4)
#%% Nesne Tabanlı Programlama

class BosAraba:
    pass # şimdilik doludurmayacağın yerlerde kullanılabilir
    
araba1 = BosAraba()


class Otobus:
    yolcular=[]
    
istanbul_otobusu = Otobus()

istanbul_otobusu.yolcular.append("Eray")

istanbul_otobusu.yolcular.append("Birgül")

istanbul_otobusu.yolcular.append("Batuhan")

istanbul_otobusu.yolcular.append("Diyar")

print(istanbul_otobusu.yolcular)

ankara_otobusu = Otobus()

print(ankara_otobusu.yolcular)

class Otobusler:
    # benzersiz bir tanımlama yapmak için
    def __init__(self,yolcular):
        self.yolcular = yolcular

otobus1_yolcular = ["Eray","Birgül"]
Otobus1 = Otobusler(otobus1_yolcular)

Otobus1.yolcular.append("Batuhan")
Otobus1.yolcular.append("Diyar")

Otobus2 = Otobusler(["Eray"])

print(Otobus2.yolcular)

Otobus2.yolcular.append("Birgül")

class Araba:
    lastik=4
    yolcular=[]
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil
        print("Araba yaratıldı")
        
araba1 = Araba("Mercedes", "C200", 2022)
araba2 = Araba("BMW","5.20",2020)       
print(araba1.marka)
print(araba2.model)

print(araba1.lastik)
print(araba2.lastik)
# Bu satır sınıftaki lastik değerini değil, sadece araba2 nesnesine özel lastik değerini 3 yapar
araba2.lastik=3

print(araba1.lastik)
print(araba2.lastik)

#print(araba2.__dict__)

araba1.yolcular.append("Eray")
print(araba1.yolcular)

araba2.yolcular.append("Birgül")
print(araba2.yolcular)

class GidenAraba:
    def __init__(self,marka,model,yil,motor):
        self.marka=marka
        self.model=model
        self.yil=yil    
        self.motor="kapalı"
        self.fren="aktif"
        
    def elfreni(self):
        self.fren="pasif"
        
    def calistir(self):
        print("Araba çalıştı, gr gr gr gr")
        self.motor="açık"
        self.elfreni()
        
    def kapat(self):
        print("Araba kapandı, brrrr")
        self.motor="kapalı"
        
        
        
gidenaraba1=GidenAraba("Audi", "A5", 2025, "")

gidenaraba1.calistir()

print(gidenaraba1.motor)

gidenaraba1.kapat()

print(gidenaraba1.motor)
        
gidenaraba2=GidenAraba("Audi", "A5", 2019, "")

print(gidenaraba2.motor)
#%% 1-Encapsulation

class BankaHesabı:
    def __init__(self,iban,isim):
        self.iban=iban
        self.tutar=0
        self.isim=isim

bh1=BankaHesabı("TR123456789","Eray")
print(bh1.tutar)
bh1.tutar=10000

class GüvenlikliBankaHesabı:
    def __init__(self,iban,isim):
        self.iban=iban
        self.__tutar=0 #Encapsulation
        self.isim=isim
    def getBakiye(self): #getter
        print("bakiyeniz :",self.__tutar)
    def setBakiye(self,miktar): #setter __setBakiye yapılırsa dışardan bu fonksiyona ulaşılamaz
        self.__tutar=self.__tutar+miktar
        print("yeni bakiyeniz :",self.__tutar)
    
gbbh1=GüvenlikliBankaHesabı("TR987654321","Ogün")
gbbh1.getBakiye()
gbbh1.setBakiye(1000)
gbbh1.getBakiye()
#%% 2-Inheritance

class Hayvan:
    def __init__(self, isim):
        self.isim = isim
        print(f"Bir hayvan oluşturuldu: {self.isim}")

class Kopek1:  # Inheritance YOK
    def __init__(self, isim):
        self.isim = isim
        print(f"Hav-hav (inheritance yok), benim adım {self.isim}")

class Kopek2(Hayvan):  # Inheritance VAR
    def __init__(self, isim):
        # Üst sınıfın (__Hayvan__) init'ini çağırıyoruz
        super().__init__(isim)
        print(f"Hav-hav (inheritance var), benim adım {self.isim}")

class Kedi(Hayvan):  # Inheritance VAR
    def __init__(self, isim):
        super().__init__(isim)
        print(f"Miyav-miyav (inheritance var), benim adım {self.isim}")


# Nesne oluşturma
kopek1 = Kopek1("Karabaş")
print()  # sadece araya boş satır

kopek2 = Kopek2("Paşa")
print()

kedi1 = Kedi("Boncuk")
#%% 3-Polymorphism

class Kopek:
    def ses_cikar(self):
        print("Hav hav")

kopek1 = Kopek()

kopek1.ses_cikar()

class Kedi():
    def ses_cikar(self):
        print("Miyav")

class Inek():
    def ses_cikar(self):
        print("Möö")

kedi1 = Kedi()

inek1 = Inek()

kedi1.ses_cikar()
inek1.ses_cikar()
#%% 4-Abstraction
from abc import ABC, abstractmethod

class Arac(ABC):
    @abstractmethod
    def gitmek(self):
        print("Arac gidiyor.")
        
class Araba(Arac):
    def gitmek(self):
        print("Arac gidiyor.")
        
#%% Numpy

import numpy as np

arr1 = np.array([1,2,3,4,5])

liste1=[1,2,3,4,5]

arr2 = np.array(liste1)

vektor=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

matris = vektor.reshape(4, 3)

matristen_vektore = matris.ravel()

print(matris.shape)
print(matris.ndim)
print(matris.dtype)
print(matris.size)

arr3 = np.array([1,2,3,4,5,"a"]) # aynı tip veriler kullanılmalı bu örnek 1,2,3,4,5'da str olarak görülüyor

# Özel matrisler
sifir_matrisi = np.zeros((3,3))

rasgele_matrisi = np.random.rand(3,4)

lin_matrisi = np.linspace(0,10,5)

a = np.array([10,20,30])
b = np.array([1,2,3])

toplama = a+b
çıkarma = a-b
çarpma = a*b
bölme = a/b

bölme_int = a//b

tmatris = matris.T

print(f"En büyük eleman, {matris.max()}")
print(f"En küçük eleman, {matris.min()}")
print(f"Ortalama , {matris.mean()}")
print(f"Toplam, {matris.sum()}")

matris[0,1] # belirli bir eleman seçimi

matris[3:] # belirli satır getir

matris[1:3,0:2] # 1'den başla 3'e git (3'ü dahil etme), 0'dan başla 2'ye git (2'yi dahil etme)

v1 = np.array([1,2])
v2 = np.array([3,4])

#Vektörlerde birleştirme
yatayvektor = np.hstack((v1,v2))
dikeyvektor = np.vstack((v1,v2))

c = np.array([1,2,3])

d = c # birbilerine bağlılar

d[0]=50

e = c.copy() # Vektörden vektör türetme

#%% Pandas

import pandas as pd

#seri = pd.Series(liste1)

harfler = pd.Series(["a","b","c"])

data = {
        "Ad":["Eray","Ogün","Birgül","Yaren","Nadi"],
        "Sehir":["Düzce","Sinop","Erzurum","İstanbul","Bolu"]
        }

df =pd.DataFrame(data)

# df'deki belirli sayıdaki ilk kaydı gösterir
df.head()
# df'deki belirli sayıdaki son kaydı gösterir
df.tail(2)
# df'deki iki tane rastgele kayır
df.sample(2)

# veri tiplerini öğrenme
df.dtypes
# df'deki kolon listesi
df.columns

# df'deki veri işlemleri
# Update
df.loc[df["Ad"]=="Eray","Sehir"] = "Kocaeli"  # verideki spesifik lokasyon

# Insert
df.loc[4] = ["Batuhan","Zonguldak"]
df.loc[5] = ["Diyar","Basel"]
df.loc[-1] = ["Deneme","Kayıt"]
df.loc[len(df)] = ["Yeni", "Kayıt"]

# Delete
df["Maas"] = 500

# axis=1->dikey, axis=0->yatay silme işleminin yansımasını istiyorsam inplace true olmalı
df.drop("Maas",axis=1,inplace=True)

df.drop(2,axis=0)

# Join
df_calisanlar = pd.DataFrame({
    "Calisan_ID": [101, 102, 103, 104],
    "Ad": ["Ali", "Veli", "Ayşe", "Fatma"],
    "BolumID": ["1", "1", "5", "3"]
})

df_bolumler = pd.DataFrame({
    "BolumID": ["1", "2", "3", "4"],
    "Bolum": ["IT", "HR", "Finance", "Legal"]
})


merge_inner=pd.merge(df_calisanlar,df_bolumler,on="BolumID",how="inner")

merge_left=pd.merge(df_calisanlar,df_bolumler,on="BolumID",how="left")

merge_right=pd.merge(df_calisanlar,df_bolumler,on="BolumID",how="right")

# Concat ama SQL'de Union olarak bilinir
df1=pd.DataFrame({"Sira":[1,2,3]})
df2=pd.DataFrame({"Sira":[4,5,6]})

# Dikey
pd.concat([df1,df2])

# Yatay
pd.concat([df1,df2], axis=1)

# Dikey+index sıfırlanarak
pd.concat([df1,df2], axis=0,ignore_index=True)
#%% Dataset çekme
import pandas as pd

df = pd.read_csv("titanic.csv", sep=",", header=0,
                 usecols=["Passengerid", "Age", "Sex", "Fare"],
                 nrows=100)

df_excel = pd.read_excel("ham_veri.xlsx",sheet_name="Rapor")

# Eksik verileri doldurma
df_excel["Fiyat"] = df_excel["Fiyat"].fillna(0)

# Kolon türetme
df_excel["ToplamTutar"] = df_excel["Fiyat"]*df_excel["Adet"]


df_filtered = df_excel[df_excel["ToplamTutar"]>100].copy()

df_filtered.to_excel("islenmis_veri.xlsx",sheet_name="Data",index=False)

df_filtered.to_excel("islenmis_veri.xlsx",sheet_name="Data")

#%% SQL Server

import sqlalchemy as sa

SERVER="DESKTOP-34ERD3"
DATABASE="dbName"
USERNAME="admin"
PASS="123456"
DRIVER="ODBC Driver 17 for SQL Server"

conn_str = f"mssql+pyodbc://{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"

#%% API Call
import pandas as pd
import requests

# GET
api_url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(api_url,timeout=10)

if response.status_code == 200:
    print("Veri başarıyla okundu", response.status_code)
    response_data = response.json()
    response_df = pd.DataFrame(response_data)
    response_df.to_excel("response_df.xlsx",index=False)

    normalize_df = pd.json_normalize(response_data)
    normalize_df.to_excel("normalize_df.xlsx",index=False)
else:
    print("İstek başarısız, hata kodu şu: ",response.status_code)

# POST
post_url = "https://jsonplaceholder.typicode.com/posts"

body = {
    "Name":"Stuart",
    "Age":15
    }

post_response = requests.post(post_url, json=body)

if post_response.status_code == 201:
    print("Veri başarıyla gönderildi", post_response.status_code)
else:
    print("İstek başarısız, hata kodu şu: ",post_response.status_code)

#%% Web Scrapping
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response_web = requests.get(url)

# tek html tag'i
if response_web.status_code == 200:
    soup=BeautifulSoup(response_web.content,"html.parser")
    
    sayfa_basligi = soup.find("h1").text
    sayfa_linkinin_style = soup.find("h1").find("a")
    sayfa_linkinin_style["style"]
    
else:
    print("siteye erişilemedi")
    
    
# birden fazla
divs = soup.find_all("div",class_ = "quote")
data_set=[]
for div in divs:
    text = div.find("span", class_="text").text
    author = div.find("small", class_="author").text
    data_set.append({"Author":author,"Text":text})

df_sozler=pd.DataFrame(data_set)
# Pagination
import time

all_pages_data=[]

page_url = "https://quotes.toscrape.com/page/"

for i in range(1,5):
    wanted_url = f"{page_url}{i}"
    time.sleep(10)
    #print(wanted_url)
    r = requests.get(wanted_url)
    s = BeautifulSoup(r.content,"html.parser")
    
    page_divs = s.find_all("div",class_ = "quote")
    
    for div in page_divs:
        text = div.find("span", class_="text").text
        author = div.find("small", class_="author").text
        all_pages_data.append({"Author":author,"Text":text})
    
df_pagination=pd.DataFrame(all_pages_data)

ibb="https://ibb.istanbul/gundem/duyurular/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
    }

r_ibb = requests.get(ibb, headers=headers)
    
if r_ibb.status_code == 200:
    s_ibb = BeautifulSoup(r_ibb.content,"html.parser")
    time.sleep(10)
    #ibb web scrapping
    
else:
    print("siteye erişilemedi")





