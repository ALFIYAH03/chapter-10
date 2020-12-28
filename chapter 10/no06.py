#chapter10
#no06

def encrypt(teks, n):
    listTeks = list(teks)

    for x in range(len(listTeks)):
        if(listTeks[x] != ''):
            if(ord(listTeks[x]) + n < 90):
               asciiCode = ord(listTeks[x])
               encrypted = asciiCode + n
               listTeks[x] = chr(encrypted)

            else:
                asciiCode = ord(listTeks[x])
                encrypted = (asciiCode + n) - 26
                listTeks[x] = chr(encrypted)

        else:
            continue

    result = ''.join(listTeks)

    return result
try:
    teks = input('Masukan teks yang ingin dienskripsi :')
    n = int (input('Berapa jumlah geseran enskripsi :'))

    hasil = encrypt(teks, n)
    print('\nHasil enkripsi dari teks {0} adalah : {1}'.format(teks, hasil))

except ValueError:
    print('Masukan khusus bilangan bulat')
