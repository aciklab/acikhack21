### String ve listelerin indekslenmesi ###

# Stringlerin İndekslenmesi

merhabaStringi = "MERHABA"
# M E R H A B A
# 0 1 2 3 4 5 6
print(merhabaStringi[-1])

# Listelerin indekslenmesi

liste1 = [0,1,2,3,4,5,6]
    # listeler 0'dan indekslenmeye başlar,
    # yani ilk elemanın indeks değeri 0'dır.

ilkEleman = liste1[0] # ilk eleman
ucuncuEleman = liste1[3] # her hangi bir eleman
sonEleman = liste1[-1] # son eleman

print(sonEleman)

# Listeye yeni eleman eklemek append()

liste1.append(7)
print(liste1)

# Listeye istenilen yerden eleman eklemek insert()

liste1.insert(0,-1) # Parametre1 : index değeri, parametre2 : eklenmek istenen değer
print(liste1)

# Listeden eleman çıkartmak

liste1.pop(0) # Parametre index değeri
print(liste1)

# Stringlerin ayrılması split()

splitString = "Çevrimiçi Pardus Yarışması Eğitimlerine Hoşgeldiniz!"
splitString2 = "Çevrimiçi Pardus Yarışması\nEğitimlerine Hoşgeldiniz!"
# Çevrimiçi Pardus Yarışması Eğitimlerine Hepiniz Hoşgeldiniz!

splitList = splitString.split()
splitList2 = splitString2.split()

print(splitList)

# Dictionary Veri tipi key - value sistemi

sozluk = {0 : "sıfır", 1 : "bir", 2 : "iki"}
sozlukAnahtarlari = sozluk.keys()
sozlukDegerleri = sozluk.values()
sozlukAnahtarVeDegerleri = sozluk.items()

print(sozluk[0])
print(sozlukAnahtarlari)
print(sozlukDegerleri)
print(sozlukAnahtarVeDegerleri)