menu = [
  ["nasi goreng",10000],
  ["es teh",5000],
  ["mie goreng",12000],
  ["bakso",10000],
  ["mie ayam",15000]

]
for i in range(5):
    print(i + 1)
    print(menu[i])
while True:
   masukan = int(input("masukan nomor:"))
   if masukan == 1:
      print(menu[0])
      break
   elif masukan == 2:
      print(menu[1])
      break
   elif masukan == 3:
      print(menu[2])
      break
   elif masukan == 4:
      print(menu[3])
      break
   elif masukan == 5:
      print(menu[4])
      break
   else:
      print("salah")