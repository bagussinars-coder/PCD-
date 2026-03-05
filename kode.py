import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(e, phi):
    gcd_val, x, y = extended_gcd(e, phi)
    return x % phi

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
while True:
    p = int(input("Masukkan bilangan prima p: "))
    if is_prime(p):
        break
    print("p bukan bilangan prima!")

while True:
    q = int(input("Masukkan bilangan prima q: "))
    if is_prime(q):
        break
    print("q bukan bilangan prima!")
    
n = p * q
phi = (p - 1) * (q - 1)

print("Nilai phi =", phi)

e = random.randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = random.randint(2, phi - 1)

d = mod_inverse(e, phi)

print("\n=== KUNCI RSA ===")
print("Public Key  (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

def encrypt(plaintext, e, n):
    cipher = []
    for char in plaintext:
        m = ord(char)
        c = pow(m, e, n)
        cipher.append(c)
    return cipher

def decrypt(ciphertext, d, n):
    plaintext = ""
    for c in ciphertext:
        m = pow(c, d, n)
        plaintext += chr(m)
    return plaintext

while True:
    print("\n=== MENU ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    choice = input("Pilih menu (1/2/3): ")

    if choice == "1":
        pesan = input("Masukkan plaintext: ")
        hasil = encrypt(pesan, e, n)
        print("Ciphertext:", hasil)

    elif choice == "2":
        data = input("Masukkan ciphertext (pisahkan dengan koma): ")
        cipher_list = list(map(int, data.split(",")))
        d_input = int(input("Masukkan kunci privat d: "))
        n_input = int(input("Masukkan nilai n: "))
        hasil = decrypt(cipher_list, d_input, n_input)
        print("Hasil dekripsi:", hasil)

    elif choice == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
