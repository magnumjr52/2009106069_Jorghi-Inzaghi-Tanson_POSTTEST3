print("Nana pergi jalan untuk membeli takoyaki. Sampai disana, tertulis harga untuk setiap isian takoyaki:")
print("Varian 1 : Rp 2000/pcs \nVarian 2 : Rp 2500/pcs")
print("Setiap hari si penjual hanya menyediakan isian varian 1 sebanyak 45 pcs dan varian 2 sebanyak 40 pcs.")
print("Keterangan :")
print("- Jika membeli 10 pcs atau lebih varian 1, harga diskon 10%")
print("- Jika membeli 8 pcs atau lebih varian 2, harga diskon 8%")
print("- Selain ketentuan diatas, harga normal")
print("")
print("Jawaban :")

harga_varian1 = 2000
harga_varian2 = 2500
pcs1 = int(input("Jumlah varian 1 yang ingin dibeli : "))
pcs2 = int(input("Jumlah varian 2 yang ingin dibeli : "))
varian1 = pcs1 * harga_varian1
varian2 = pcs2 * harga_varian2

if pcs1 <= 45 and pcs2 <= 40:
    if pcs1 < 10 and pcs2 < 8:
        print("Nana harus membayar takoyaki tersebut sebesar Rp %s" % (varian1 + varian2))
    elif pcs1 >= 10 and pcs2 >= 8:
        diskon1 = varian1 - (varian1 * 0.1)
        diskon2 = varian2 - (varian2 * 0.08)
        print("Nana harus membayar takoyaki tersebut sebesar Rp %s" % (diskon1 + diskon2))
    elif pcs1 >= 10 and pcs2 < 8:
        diskon1 = varian1 - (varian1 * 0.1)
        print("Nana harus membayar takoyaki tersebut sebesar Rp %s" % (diskon1 + varian2))
    elif pcs1 < 10 and pcs2 >= 8:
        diskon2 = varian2 - (varian2 * 0.08)
        print("Nana harus membayar takoyaki tersebut sebesar Rp %s" % (varian1 + diskon2))
    else:
        print("Stok takoyaki tidak cukup")
else:
    print("Isi jumlah varian 1 dan/atau 2 yang ingin dibeli dengan benar")