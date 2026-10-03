class produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama : {self.nama}")
        print(f"Harga : Rp{self.harga}")

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 5 / 100
        else:
            return 0

