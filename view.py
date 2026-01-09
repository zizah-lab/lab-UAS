class ViewMahasiswa:
    def tampilkan_tabel(self, mhs):
        print("\n======= DATA MAHASISWA =======")
        print(f"{'NIM':<15}{'Nama':<20}{'Nilai':<10}{'Grade':<10}{'Status'}")
        print("=" * 60)
        print(f"{mhs.nim:<15}{mhs.nama:<20}{mhs.nilai:<10}{mhs.get_grade():<10}{mhs.get_status()}")
        print("=" * 60)