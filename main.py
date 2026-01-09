from process import ProsesMahasiswa
from view import ViewMahasiswa
nim = input("Masukkan NIM :")
nama = input("Masukkan Nama :")
nilai = float(input("Masukkan Nilai: "))

proses = ProsesMahasiswa()
view = ViewMahasiswa()

mhs = proses.buat(nim, nama, nilai)
view.tampilkan_tabel(mhs)