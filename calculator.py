def menu():
    print("\n\t1.+\n\t2.-\n\t3.X\n\t4.EXIT")


def tambah():
    a=int(input("Masukan Nomor: "))
    b=int(input("Masukan Nomor: "))
    hasil=a+b
    print("Hasil Pertambahan:",hasil)

def kali():
    a=int(input("Masukan Nomor: "))
    b=int(input("Masukan Nomor: "))
    hasil=a*b
    print("Hasil Perkalian:",hasil)

def kurang():
    a=int(input("Masukan Nomor: "))
    b=int(input("Masukan Nomor: "))
    hasil=a-b
    print("Hasil Perkalian:",hasil)


menu()
pil = int(input("Masukan Operator: "))
while pil >=1 and pil <=3:
    if pil == 1:
        tambah()
    elif pil == 2:
        kurang()
    elif pil == 3:
        kali()
    elif pil == 4:
        pil = 6
    menu()
    pil = int(input("Masukan Operator: "))
print("Berhasil Keluar")