import numpy as np
import matplotlib.pyplot as plt

rowmax = 1879  # Tidak perlu menggunakan fungsi int karena sudah berupa integer
colmax = 1919  # Tidak perlu menggunakan fungsi int karena sudah berupa integer
radius_max = 1000
batas1 = int(0.2 * radius_max)
batas2 = int(0.4 * radius_max)
batas3 = int(0.6 * radius_max)
batas4 = int(0.8 * radius_max)

Gambar = np.zeros(shape=(rowmax + 1, colmax + 1, 3), dtype=np.uint8)

for i in range(0, rowmax + 1):
    for j in range(0, colmax + 1):
        if (i ** 2 + j ** 2) >= 0 and (i ** 2 + j ** 2) < batas1 ** 2:
            Gambar[i, j, 0] = 255  # Merah
        if (i ** 2 + j ** 2) >= batas1 ** 2 and (i ** 2 + j ** 2) < batas2 ** 2:
            Gambar[i, j, 1] = 255  # Hijau
        if (i ** 2 + j ** 2) >= batas2 ** 2 and (i ** 2 + j ** 2) < batas3 ** 2:
            Gambar[i, j, 2] = 255  # Biru
        if (i ** 2 + j ** 2) >= batas3 ** 2 and (i ** 2 + j ** 2) < batas4 ** 2:
            Gambar[i, j, 0] = 255  # Merah
            Gambar[i, j, 1] = 255  # Hijau
        if (i ** 2 + j ** 2) >= batas4 ** 2 and (i ** 2 + j ** 2) < radius_max ** 2:
            Gambar[i, j, 0] = 255  # Merah
            Gambar[i, j, 2] = 255  # Biru

plt.figure()
plt.imshow(Gambar)
plt.show()
