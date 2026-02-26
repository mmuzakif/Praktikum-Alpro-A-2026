
class NamaError(Exception):
    def __init__(self,nama):
        self.nama = nama
        super().__init__("nama kurang panjang(huruf maksimal 3 karakter)")
def validasi_nama(nama):
    nama_len = len(nama)
    if nama_len <= 2:
        raise NamaError(nama)
    return True
class Umur(Exception):
    def __init__(self,umur):
        self.umur = umur
        super().__init__("umur tidak memunuhi syarat (17-60)")
def validasi_umur(umur):
    if umur < 17 or umur > 60:
        raise Umur(umur)
    return True
class Email(Exception):
    def __init__(self,email):
        self.email = email
        super().__init__("email salah,harus mengandung @ dan .com")
def validasi_email(email):
    if "@" not in email or ".com" not in email:
        raise Email(email)
    return True
class Nomor(Exception):
    def __init__(self,nomor):
        self.nomor = nomor
        super().__init__("nomor harus mengandung 10-13 digit angka")
def validasi_nomor(nomor):
    nomor1 = len(nomor)
    if nomor1 < 10 or nomor1 > 13:
        raise Nomor(nomor)
    return True

while True:
     try:      
       nama = input("masukan nama:")
       validasi_nama(nama)
       break
     except NamaError as e:
       print("error,",e)
while True:
    try:
        umur = int(input("masukan umur kamu:"))
        validasi_umur(umur)
        break
    except Umur as e:
        print("error = ",e) 
while True:
    try:
        email = input("masukan email:")
        validasi_email(email)
        break
    except Email as e:
        print("error = ",e)
while True:
    try:
        nomor = input("masukan no hp:")
        validasi_nomor(nomor)
        break
    except Nomor as e:
        print("error = ",e)
        
print("=== Data Peserta ===")   
print("nama =",nama)
print("umur = ",umur)
print("email = ",email)
print("nomor hp = ",nomor)
print("status = Terdaftar")
     
    

  







