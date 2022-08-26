a = ["apple", "banana", "cherry"]
print(a[-3]) #mangilnya dari belakang
print(a[0]) #manggilnya dari depan
print(a[1:2]) #manggilnya dari depan

#ubah value array / list
thislist = ["apple", "banana", "cherry"]
thislist[0] = "blackcurrant"
print(thislist)

#tambah value 
c = ['coba', 'test', 'isi']
c.append('jeruk')
print(c)
c.insert(1, 'mangga')
print(c)
d = ['motor', 'mobil']
c.extend(d)
print(c)

#hapus array
c.remove('mobil')
print(c)
c.pop(1)
print(c)
c.pop() #jika kosong maka akan di hapus yg paling akhir
print(c) 
# c.clear()
# print(c)

#loop
for x in c:
    print(x)

print("")

for i in range(len(c)) :
    print(c[i])

print("")

j = 0
while j < len(c) :
    print(c[j])
    j = j + 1


print("")

[print(h) for h in c]

#perbedaan tuple list dan sets adalah () , [], {}
