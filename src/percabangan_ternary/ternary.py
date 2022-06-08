    kondisi = True
    print(2 if kondisi else 1/0)
    #Output is 2

    print((1/0, 2)[kondisi])
    #Eror Pembagian Nol akan muncul
