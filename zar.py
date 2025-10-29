import random 

def zar_at():
    return random.randint(1,6)

adet = int(input("Zarı kaç kez atmak istersiniz?:"))

sonuçlar = []

for i in range (adet):
    sonuç=zar_at()
    sonuçlar.append(sonuç)

print("Sonuçlar:" , sonuçlar)

from collections import Counter

frekanslar = Counter(sonuçlar)
print("Frekanslar:" , frekanslar)

en_çok_gelen = frekanslar.most_common(1)[0][0]
print("En çok gelen sayı:" , en_çok_gelen)

from statistics import mean 

ortalama = mean(sonuçlar)
print("Ortalama zar değeri:" , ortalama)