#Learning Python
#Made By Jesen-N

import os, sys

def pertambahan():
    os.system('cls')
    print("""Pertambahan = a + b
    """)
    a = int(input("Masukan Nomor a: "))
    b = int(input("Masukan Nomor b: "))
    print("")
    asu = a + b
    print (f"Hasil: {a} + {b} = " + str(asu))
    print("")
    y = input("Kembali Ke Menu Awal? (y/n): ")
    if y == "y":
        menu()

def perkurangan():
    os.system('cls')
    print("""Perkurangan = a - b
    """)
    a = int(input("Masukan Nomor a: "))
    b = int(input("Masukan Nomor b: "))
    print("")
    asu = a - b
    print (f"Hasil: {a} - {b} = " + str(asu))
    print("")
    y = input("Kembali Ke Menu Awal? (y/n): ")
    if y == "y":
        menu()
    
def perkalian():
    os.system('cls')
    print("""Perkalian = a x b
    """)
    a = int(input("Masukan Nomor a: "))
    b = int(input("Masukan Nomor b: "))
    print("")
    asu = a * b
    print (f"Hasil: {a} x {b} = " + str(asu))
    print("")
    y = input("Kembali Ke Menu Awal? (y/n): ")
    if y == "y":
        menu()

def pembagian():
    os.system('cls')
    print("""Pembagian = a ÷ b
    """)
    a = int(input("Masukan Nomor a: "))
    b = int(input("Masukan Nomor b: "))
    print("")
    asu = a // b
    print (f"Hasil: {a} ÷ {b} = " + str(asu))
    print("")
    y = input("Kembali Ke Menu Awal? (y/n): ")
    if y == "y":
        menu()

def pangkat():
    os.system('cls')
    print("""Pangkat = a pangkat b
    """)
    a = int(input("Masukan Nomor a: "))
    b = int(input("Masukan Nomor b: "))
    print("")
    asu = a ** b
    print (f"Hasil: {a} pangkat {b} = " + str(asu))
    print("")
    y = input("Kembali Ke Menu Awal? (y/n): ")
    if y == "y":
        menu()

def menu():
    os.system('cls')
    print("""
    
███╗░░░███╗████████╗██╗░░██╗
████╗░████║╚══██╔══╝██║░██╔╝
██╔████╔██║░░░██║░░░█████═╝░
██║╚██╔╝██║░░░██║░░░██╔═██╗░
██║░╚═╝░██║░░░██║░░░██║░╚██╗
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

==========================================
 [>] Made By Jesen-N
 [>] Github : https://github.com/Jesen-N
==========================================
    Menu:
    1. Pertambahan
    2. Perkurangan
    3. Perkalian
    4. Pembagian
    5. Pangkat
""")

    menu = input("[>] Pilih Menu: ")

    if menu == "1":pertambahan()
    elif menu == "2":perkurangan()
    elif menu == "3":perkalian()
    elif menu == "4":pembagian()
    elif menu == "5":pangkat()
    else:
        print("Menu Tidak Ada!")
        input("Press Enter To Exit...")

menu()
