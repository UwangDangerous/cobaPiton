# class MyClass:
#     x = 5

# # print (MyClass)

# p1 = MyClass()
# print(p1.x)


class Test:
    def __init__(objek, nama, no):
        objek.nama = nama
        objek.no = no


    def Fungsi(a):
        print("Hello", a.nama, " No.", a.no)

    def kosong():
        pass

p1 = Test("coba", 12)
p1.Fungsi()