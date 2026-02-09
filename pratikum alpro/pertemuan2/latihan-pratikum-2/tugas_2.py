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
    pass_len = len(password)
    h = upper(password)
    if password <= pass_len:
        if password not in h:
            if password in '1' and '9':
                if password





is_password_valid("Password123")
is_password_valid("password")

#no 3
def hitung_nilai(tugas,uts,uas)

