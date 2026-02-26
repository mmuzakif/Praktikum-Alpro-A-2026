"""
angka_list = [10, 20, 30]
try:
   idx = int(input('Masukkan index (0-2): '))
   print(f'Nilai: {angka_list[idx]}')
except ValueError:
   print('Harus berupa angka bulat!')
except IndexError:
   print('Index di luar jangkauan!')
finally: 
   print('Selesai.')
"""



try:
    masukan_1 = int(input("masukan angka pertama:"))
    masukan_2 = int(input("masukan angka kedua:")) 
    kalkulasi = masukan_1 / masukan_2
    print(kalkulasi)
except ValueError:
   print("harus berupa angkat bulat")
except ZeroDivisionError:
   print("bagi dengan angka selain 0")
except TypeError:
   print("type salah")


