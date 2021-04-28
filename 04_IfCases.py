# python3
# Get inputs from user
name = input("Lutfen isminizi giriniz: ")
print("Merhaba " + name)
age = input("Lutfen yasinizi giriniz: ")

# Check user input 
isString = isinstance(name, str)
if isString:
    print(name + " bir stringdir.")
else :
    print(name + " bir string degildir.")
    
# Check user input 
isInt = isinstance(age, int)
if not isInt:
    print("Lutfen bir sayi girin.")
else : 
    print(str(age) + " bir sayidir.")

# Advance - Casting Try Catch
try:
    int_name = int(name)
except:
    print(name + " integer cevrilemez.")

# If check
ageLimit = 18
if age > ageLimit:
    print("Yasiniz araba kullanamya uygun.")
elif age == ageLimit: 
    print("Artik ehliyet alabilirsiniz.")
else :
    print("Araba kullanmak icin buyumeniz lazim.")


answer = input("Ehliyetiniz var mi, evet/hayir yazin:")
if not (answer == "evet" or answer == "hayir"):
    print("Gecerli bir deger girmediniz")
    exit()

if answer == "evet" and age >= ageLimit:
    print("Trafige cikabilirsiniz.")
elif answer == "evet" and age < ageLimit:
    print("Girdiginiz bilgilerde bir celiski var.")
elif answer == "hayir":
    print("Once ehliyet almalisiniz.")

