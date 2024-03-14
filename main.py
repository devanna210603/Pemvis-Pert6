#Latihan Set (minimal 5)
#Alur cerita.Case: Buah,Makanan,Pakaian dan aksesoris,Belanja/bahan pokok,Penjulan sesuatu,dll.

class TokoBuah:
    def __init__(self):
        self.daftar_buah = set()

    def tambah_buah(self, buah):
        self.daftar_buah.add(buah)
        print(f"Selamat datang di toko buah kami!")
        print(f"{buah} telah ditambahkan ke dalam daftar buah.")

    def cek_daftar_buah(self):
        print("Selamat datang di toko buah kami!")
        print("Daftar buah saat ini:")
        for buah in self.daftar_buah:
            print("-", buah)

    def jumlah_buah(self):
        print("Selamat datang di toko buah kami!")
        print(f"Jumlah buah dalam daftar: {len(self.daftar_buah)}")

    def update_buah(self, buah_lama, buah_baru):
        if buah_lama in self.daftar_buah:
            self.daftar_buah.remove(buah_lama)
            self.daftar_buah.add(buah_baru)
            print("Selamat datang di toko buah kami!")
            print(f"{buah_lama} telah diperbarui menjadi {buah_baru}.")
        else:
            print("Selamat datang di toko buah kami!")
            print(f"{buah_lama} tidak ditemukan dalam daftar buah.")

    def hapus_buah(self, buah):
        if buah in self.daftar_buah:
            self.daftar_buah.remove(buah)
            print("Selamat datang di toko buah kami!")
            print(f"{buah} telah dihapus dari daftar buah.")
        else:
            print("Selamat datang di toko buah kami!")
            print(f"{buah} tidak ditemukan dalam daftar buah.")


# Alur Cerita
toko_buah = TokoBuah()

# Tambah buah
toko_buah.tambah_buah("Apel")
toko_buah.tambah_buah("Jeruk")
toko_buah.tambah_buah("Pisang")

# Cek daftar buah
toko_buah.cek_daftar_buah()

# Jumlah buah dalam daftar
toko_buah.jumlah_buah()

# Update buah
toko_buah.update_buah("Jeruk", "Anggur")

# Hapus buah
toko_buah.hapus_buah("Pisang")

# Cek daftar buah setelah perubahan
toko_buah.cek_daftar_buah()

# Jumlah buah dalam daftar setelah perubahan
toko_buah.jumlah_buah()
