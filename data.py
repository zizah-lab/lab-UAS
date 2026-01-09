class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

    def get_grade(self):
        if self.nilai >= 85:
            return 'A'
        elif self.nilai >= 70:
            return 'B'
        elif self.nilai >= 60:
            return 'C'
        elif self.nilai >= 50:
            return 'D'
        else:
            return 'E'

    def get_status(self):
        return 'LULUS' if self.nilai >= 60 else 'TIDAK LULUS'