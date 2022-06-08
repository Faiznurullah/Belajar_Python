

      class KalkulatorKali(Kalkulator):
        """contoh mewarisi kelas kalkulator sederhana"""

        def kali_angka(self, angka1, angka2):
            self.nilai = angka1 * angka2
            return self.nilai

        def tambah_angka(self, angka1, angka2):
            self.nilai = angka1 + angka2
            return self.nilai



    kk = KalkulatorKali()
    b = kk.tambah_angka(5, 6)  # fitur tambah_angka yang dipanggil milik KalkulatorKali
    print(b)
