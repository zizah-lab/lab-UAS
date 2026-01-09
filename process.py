from data import Mahasiswa

class ProsesMahasiswa:
    def buat(self, nim, nama, nilai):
        return Mahasiswa(nim, nama, nilai)