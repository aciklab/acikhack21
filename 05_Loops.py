# For loop
num1 = int(input("Bir sayi giriniz: "))

count = 1
while count <= num1:
    print(count)
    count += 1  
    
# 5 x 4
num2 = int(input("İkinci bir sayi giriniz: "))
count = 0
result = 0

# Multiply with while
while count < num1:
    result += num2
    count += 1
print(str(num1) + " * " + str(num2) + " = " + str(result))

# Multiply with for
result = 0
for i in range(0, num1):
    result += num2
print(str(num1) + " * " + str(num2) + " = " + str(result))

# For loop with array
fruits = ["elma", "muz", "kivi", "erik"]
for x in fruits:
  print(x)

# Does contains with for loop
flag = False
key = input("Meyve adi girin: ")
for x in fruits:
    if x == key:
        # print("Kivi array'de var.")
        flag = True
        break
if flag: 
    print(key + " arrayde var.")
else:
    print(key + " arrayde yok.")

# Does contains with for loop
location = -1
key = input("Meyve adi girin: ")
for index,x in enumerate(fruits):
    if x == key:
        location = index
        break
print(key + " indexi " + str(location))

for i in range(0, 5):
    if i == 3:
        continue
    print(i)

numbers = [1.73, 1.68, 1.71, 1.89]
for num in numbers:
    print(num)
