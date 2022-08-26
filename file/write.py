i = input("Nama File : ") 
f = open(i+".txt", "w")
isi = input("isi : ")
f.write(isi)
f.close()

#open and read the file after the appending:
f = open(i+".txt", "r")
print(f.read())