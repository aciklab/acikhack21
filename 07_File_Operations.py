# r  , okuma.
# w  , yazma.
# a  , sondan ekleme.
# r+ , okuma ve yazma


f = open("test.txt",'w')
f.write("1-Dosyaya boyle yazdirilir.\n")
f.close()

f = open("test.txt",'w')
f.write("2-Dosya islemlerinde uzerine yazmamak onemli.\n")
f.close()

f = open("test.txt",'a')
f.write("3-Sonuda eklenmeli.\n")
f.close()

file = open('test.txt', 'r')
print(file.read())
file.close()


file = open('test.txt', 'r')
for word in file:
    print(word)
file.close()


file = open('test.txt', 'r')
line = file.readline(10)
while line != '':  # The EOF char is an empty string
    print(line, end='@')
    line = file.readline(10)
file.close()

file = open('test.txt', 'a+')
line = file.readline(10)
while line != '':  # The EOF char is an empty string
    print(line, end='\n')
    line = file.readline(10)
file.close()

with open("welcome.txt","w") as file2: # Use file to refer to the file object
   file2.write("example\n")
   file2.write("example1")
   file2.writelines(["ornek", "metin"])

with open("welcome.txt","r") as file3: # Use file to refer to the file object
    data = file3.read()
    print(data)

# read tum sayfayi okur
# readline satir satir okur
# readlines array olarak okur
