def DoesContain():
    pass

def FindIndex(item,array):
    location = -1
    for index,x in enumerate(array):
        if x == item:
            location = index
            break

    return location

fruits = ["elma", "muz", "kivi", "erik"]
print(FindIndex("kivi", fruits))
print(DoesContain())

# Pass by value
text = "Orjinal metin"
def test(text):
    string = "Modifiye edildi"
    print("Fonksiyon icerisinde:", text)
test(text)
print("Fonksiyon disinda:", text)

# Pass by reference
def AddToArray(list,number):
    list.append(number)
    print("Fonksiyon icerisinde", list)
mylist = [10,20,30,40]
AddToArray(mylist,50)
print("Fonksiyon disinda:", mylist)

# Pass by reference for string
textArray = ["Orjinal metin"]
def ChangeString(textArray):
    textArray[0] = "Modifiye edildi"
    print("Fonksiyon icerisinde", textArray)
ChangeString(textArray)
print("Fonksiyon disinda:", textArray)