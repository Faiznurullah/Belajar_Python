
    class Kalkulator:
        """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""

        def __init__(self, nilai=0):
            self.nilai = nilai

        def tambah_angka(self, angka1, angka2):
            self.nilai = angka1 + angka2
            if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
                print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
            return self.nilai


    b = kk.tambah_angka(5, 6)  # memiliki fitur tambah_angka karena mewarisi dari Kalkulator
    print(b)        
