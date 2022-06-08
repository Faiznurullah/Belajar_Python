
 try:
     with open('contoh_tidak_ada.py') as file:
        print(file.read())
 except (FileNotFoundError, ):
    print('file tidak ditemukan')

//

    >>> d = {'ratarata': '10.0'}
    >>> try:
    ...     print('rata-rata: {}'.format(d['rata_rata']))
    ... except KeyError:
    ...     print('kunci tidak ditemukan di dictionary')
    ... except ValueError:
    ...     print('nilai tidak sesuai')
    ...
    kunci tidak ditemukan di dictionary
    >>> try:
    ...     print('rata-rata: {}'.format(d['ratarata']/3))
    ... except KeyError:
    ...     print('kunci tidak ditemukan di dictionary')
    ... except (ValueError, TypeError):
    ...     print('nilai atau tipe tidak sesuai')
    ...
    nilai atau tipe tidak sesuai
    >>> try:
    ...     print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
    ... except (ValueError, TypeError) as e:
    ...     print('penangan kesalahan: {}'.format(e))
    ...
    penangan kesalahan: invalid literal for int() with base 10: '10.0'
