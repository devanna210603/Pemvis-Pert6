#Latihan Set (minimal 5)
#Alur cerita.Case: Buah,Makanan,Pakaian dan aksesoris,Belanja/bahan pokok,Penjulan sesuatu,dll.

class Toko:
    def _init_(self, nama):
        self.nama = nama

    def belanja(self, kategori):
        print(f"Selamat datang di {self.nama}!")
        print(f"Silakan pilih dari kategori {kategori}:")
        print("1. Apel")
        print("2. Pisang")
        print("3. Jeruk")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            print("Anda memilih apel.")
        elif pilihan == "2":
            print("Anda memilih pisang.")
        elif pilihan == "3":
            print("Anda memilih jeruk.")
        elif pilihan == "4":
            print("Terima kasih telah berbelanja di toko kami!")
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
            self.belanja(kategori)

    def penjualan(self, item):
        print(f"Selamat datang di {self.nama}!")
        print(f"Terima kasih atas pembelian Anda.")
        print(f"Anda telah membeli {item}.")

    def cetak(self, pesan):
        print(pesan)


# Alur Cerita
toko = Toko("Toko Buah Segar")

# Belanja buah
toko.belanja("buah")

# Penjualan
toko.penjualan("apel")

# Alur Cerita lainnya
toko.cetak("Alur cerita lainnya...")
