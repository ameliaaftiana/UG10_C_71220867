print ("========== Pilih menu ==========")
print ("1. Tambah")
print ("2. Kurang")
print ("3. Kali")
print ("4. Bagi")

bil1= int(input ("Masukkan angka pertama: "))
bil2= int(input ("Masukkan angka kedua: "))

pilihan= int(input ("Pilihan Anda: "))


if pilihan == 1:
    print ("hasil= ", bil1 + bil2)
elif pilihan == 2:
    print ("hasil= ", bil1 - bil2)
elif pilihan == 3:
    print ("hasil= ", bil1 * bil2)
elif pilihan == 4:
    print ("hasil= ", bil1 / bil2)



