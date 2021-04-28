### Matematik Operatörleri ###
# +,-,/,*

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(12 / 3)

# String toplama
parca1 = "Merhaba ben Çevrimiçi Pardus "
parca2 = "yarışmasına katılacağım."

parca3 = parca1 + parca2
print(parca1 + parca2)

##### Format fonksiyonu neden kullanılmalı ?

ilkDegisken = 3
ikinciDegisken = 4
toplam = ilkDegisken + ikinciDegisken

# toplamaString = "İlk sayımız " + ilkDegisken + " ikinci sayımız ise " + ikinciDegisken + "dir."
# toplamaString2 = "Bu sayıların toplamı ise " + toplam

# print(toplamaString + toplamaString2)
# ERROR : String ile int veri tipi toplanamaz !

toplamaString = "İlk sayımız {}, ikinci sayımız ise {}'dir. Bu sayıların toplamı ise {}'dır.".format(ilkDegisken,ikinciDegisken,toplam) 
print(toplamaString)
