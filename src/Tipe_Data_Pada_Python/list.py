    
    x = [5,10,15,20,25,30,35,40]
    print(x[5])
    print(x[-1])
    print(x[3:5])
    print(x[:5])
    print(x[-3:])
    print(x[1:7:2])
    
    // 
    
    x = [1,2,3]
    x[2]=4
    print(x)
    
    //
    
    x = [1,2,3]
    x[2]=4
    x.append(5)
    print(x)
    
    //
    
    binatang = ['kucing', 'rusa', 'badak', 'gajah']
    del binatang[2]
    print(binatang)
    
    //
    
    s = "Hello World!"
    print(s[4]) 		#ambil karakter kelima dari string s
    print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
    s[5]="d" 		#ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
    s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
    print(s)
