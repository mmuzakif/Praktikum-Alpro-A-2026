class Kawan:
    def __init__(self,nama,umur,tinggi):
        self.nama = nama
        self.umur = umur
        self.tinggi = tinggi
    def pertambahan(umur1,umur2):
        print("hasil tambah dari umur muzaki dan fahrul =",umur1 + umur2)
    def pengurangan(umur1,umur2):
        print("hasil pengurangan umur fahrul dan angga =",umur1 - umur2)
    def ubah_nama(self,ubah):
        self.nama = ubah

calc = Kawan
p1 = Kawan("muzaki",20,165)
p2 = Kawan("fahrul",19,160)
p3 = Kawan("angga",19,170)

print(p1.nama,p1.umur)
print(calc.pertambahan(p1.umur,p2.umur))
print(calc.pengurangan(p2.umur,p3.umur))
print("nama lama",p1.nama)
p1.ubah_nama("gama")
print("nama baru",p1.nama)
print("nama kedua",p2.nama)