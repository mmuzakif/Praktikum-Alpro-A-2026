# no 1
def fizzbuzz_plus(n):
    result_function = ""
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print ("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i % 7 == 0:
            print("seven")
        elif i % 3 == 0 and i % 7 == 0:
            print("FizzSeven")
        elif i % 5 == 0 and i % 7 == 0:
            print("BuzzSeven")
        elif i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i)
        i += 1

r = 21
fizzbuzz_plus(r)

#no 2
def is_password_valid(password):
    password_len = len(password)
    password_up = password.upper()
    check_h = False
    has_number = any(char.isdigit() for char in password)
    if password_len > 8:
        for i in range(password_len):
            for j in range(password_len):
                if password[i] == password_up[j]:
                    check_h = True 
                    break
        if has_number == True:
            if " " not in password:
                print("true")
                
    else:
        print("invalid")






is_password_valid("Password123")
is_password_valid("password")

#no 3
#Tugas: 30%
#UTS: 30%
#UAS: 40%
"""
≥ 85 A
≥ 70 B
≥ 55 C
≥ 40 D
< 40 E
"""
def hitung_nilai(tugas,uts,uas):
    hasil_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
    if hasil_akhir >= 85:
        print("A")
    elif hasil_akhir >= 70:
        print("b")
    elif hasil_akhir >= 55:
        print("c")
    elif hasil_akhir >= 40:
        print("d")
    else:
        print("e")

hitung_nilai(80,75,90)

