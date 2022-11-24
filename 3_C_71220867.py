pesanan= str(input("Masukkan daftar pesanan : "))
daftar= pesanan.split(',')
bur= [i.title() for i in daftar]
print ("Daftar pesanan : ", bur)
tambahan= str(input("Masukkan pesanan yang ingin ditambahkan : "))

if tambahan in daftar :
    print (tambahan.upper() , "sudah berada dalam daftar pesanan")
else :
    daftar.append(tambahan)
    print ("Hasil penambahan pada daftar pesanan : " , daftar)
