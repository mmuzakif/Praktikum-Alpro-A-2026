menu = [
  ["nasi goreng",10000],
  ["es teh",5000],
  ["mie goreng",12000],
  ["bakso",10000],
  ["mie ayam",15000]
]

menu1 =[0,0,0,0,0]
harga = 0
for i in range(5):
    print(i + 1)
    print(menu[i])
i = 0
while True:
    masukan = int(input("masukan  pesanan / 0:"))
    if masukan == 1:
        print("pesanan =",menu[0])
        harga += 10000
        b = masukan - 1
    elif masukan == 2:
        print("pesanan = ",menu[1])
        harga += 5000
        b = masukan - 1
    elif masukan == 3:
        print("pesanan = ",menu[2])
        harga += 12000
        b = masukan - 1
    elif masukan == 4:
        print("pesanan = ",menu[3])
        harga += 10000
        b = masukan - 1
    elif masukan == 5:
        print("pesanan = ",menu[4])
        harga += 15000
        b = masukan - 1
    elif masukan == 0:
        print("terimakasih")
        break
    menu1[i] = b
    i += 1

h = len(menu1)
for k in range(i):
    h = menu1[k]
    print("pesanan = ",menu[h])
print("total = ",harga)

while True:
    bayar = int(input("bayar:"))
    if bayar > harga:
        hasil =   bayar - harga
        print("total belanjann = ",harga)
        print("uang kamu = ",bayar)
        print("total kembalian = ",hasil)
        break
    elif bayar < harga:
        print("uang tidak cukup")