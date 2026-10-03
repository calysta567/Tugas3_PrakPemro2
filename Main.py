from Calysta import produk

jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

total_semua = 0

for i in range(jumlah_produk):
    print(f"\nProduk ke-{i + 1}")

    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))
    jumlah = int(input("Masukkan jumlah beli: "))

    produk1 = produk(nama, harga)

    produk1.tampilkan_info()

    total_produk = produk1.hitung_total(jumlah)

    print(f"Total {nama} : Rp{total_produk}")

    total_semua += total_produk


diskon = produk1.hitung_diskon(total_semua)
total_bayar = total_semua - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : Rp{total_semua}")
print(f"Diskon 5%       : Rp{diskon:.0f}")
print(f"Total Bayar     : Rp{total_bayar:.0f}")