
porsi = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

hari = ["b",'b','b','b']
hari_counter = 0
porsi_counter = 0
i = 0
while True:
   masukan = input("masukan hari / stop :")
   if masukan == "stop":
      print("selesai")
      break
   hari_counter += 1
   hari[i] = masukan  
   k = 0
   while True:
     g = int(input("masukan porsi / 0 :"))
     if g == 0:
        break
     porsi[i][k] = g
     k += 1
     porsi_counter += 1
   i += 1
j = 0
while g < hari_counter:
   e = 0
   print(hari[g])
   while j < porsi_counter and porsi[g][e] != 0:
      print(porsi[g][e])
      e += 1
      j += 1
   g += 1
      








    



