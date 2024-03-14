# Fungsi untuk menghitung PPN
def hitung_ppn(nilai):
    if nilai > 10000:
        return nilai * 0.12
    else:
        return 0

# Input nilai a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
a_lebih_besar_dari_b = a > b

# Cek apakah b lebih besar dari a
b_lebih_besar_dari_a = b > a

# Cek apakah a sama dengan b
a_sama_dengan_b = a == b

# Hitung PPN a dan b
ppn_a = hitung_ppn(a)
ppn_b = hitung_ppn(b)

# Tambahkan kedua PPN
total_ppn = ppn_a + ppn_b

# Hapus nilai a dan b
del a
del b

# Cek apakah nilai a dan b masih ada
nilai_a_masih_ada = 'a' in locals() or 'a' in globals()
nilai_b_masih_ada = 'b' in locals() or 'b' in globals()

# Output
print("Apakah nilai a lebih besar dari b?", a_lebih_besar_dari_b)
print("Apakah nilai b lebih besar dari a?", b_lebih_besar_dari_a)
print("Apakah nilai a sama dengan b?", a_sama_dengan_b)
print("PPN a:", ppn_a)
print("PPN b:", ppn_b)
print("Total PPN:", total_ppn)
print("Apakah nilai a masih ada?", nilai_a_masih_ada)
print("Apakah nilai b masih ada?", nilai_b_masih_ada)
